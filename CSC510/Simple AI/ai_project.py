import collections

def calculate_posterior(priors, likelihoods, observed_symptoms):
    """
    Calculates the posterior probability of each disease given observed symptoms.

    Args:
        priors (dict): A dictionary where keys are disease names (str) and
                       values are their prior probabilities (float).
        likelihoods (dict): A nested dictionary where the outer keys are disease names (str),
                            and the inner keys are symptom names (str), with values
                            being the likelihood P(Symptom|Disease) (float).
        observed_symptoms (list): A list of symptom names (str) that have been observed.

    Returns:
        dict: A dictionary where keys are disease names and values are their
              posterior probabilities (float), normalized to sum to 1.
    """
    posterior_unnormalized = collections.defaultdict(float)

    for disease, prior_prob in priors.items():
        # Start with the prior probability
        disease_probability = prior_prob

        # Multiply by the likelihood of each observed symptom
        for symptom in observed_symptoms:
            if disease in likelihoods and symptom in likelihoods[disease]:
                disease_probability *= likelihoods[disease][symptom]
            else:
                # If a symptom is not defined for a disease, assume its likelihood is 0
                # or a very small number to avoid division by zero later.
                # For simplicity, we'll just set the disease probability to 0 here
                # if a symptom isn't defined.
                disease_probability = 0
                break # No need to check other symptoms if one is impossible
        posterior_unnormalized[disease] = disease_probability

    # Normalize the probabilities
    total_probability = sum(posterior_unnormalized.values())
    posterior_normalized = {}
    if total_probability > 0:
        for disease, prob in posterior_unnormalized.items():
            posterior_normalized[disease] = prob / total_probability
    else:
        # Handle cases where no diseases match, or all probabilities are zero
        # This might happen if the observed symptoms are contradictory to all diseases.
        print("Warning: No diseases match the observed symptoms with non-zero probability.")
        # You might want to assign equal low probabilities or just return zeros here.
        # For this example, we'll return zeros for all.
        for disease in priors.keys():
            posterior_normalized[disease] = 0.0

    return posterior_normalized

def get_user_symptoms(available_symptoms):
    """
    Prompts the user to enter observed symptoms.
    """
    observed = []
    print("\nPlease enter the symptoms you are observing (type 'done' when finished):")
    print("Available symptoms: " + ", ".join(available_symptoms))

    while True:
        symptom = input("Symptom: ").strip().lower()
        if symptom == 'done':
            break
        elif symptom in available_symptoms:
            if symptom not in observed:
                observed.append(symptom)
            else:
                print(f"'{symptom}' already added.")
        else:
            print(f"'{symptom}' is not a recognized symptom. Please try again.")
    return observed

def main():
    """
    Main function to run the interactive medical diagnosis script.
    """
    print("Welcome to the Bayesian Medical Diagnosis System!")
    print("This program will help estimate the probability of certain diseases")
    print("based on the symptoms you provide.")

    # 1. Define Priors (P(Disease))
    # These are illustrative probabilities. In a real system, these would come from
    # epidemiological data.
    priors = {
        "flu": 0.05,        # 5% chance of having flu in the general population
        "common cold": 0.20,  # 20% chance of having common cold
        "allergies": 0.15,   # 15% chance of having allergies
        "pneumonia": 0.01,   # 1% chance of having pneumonia (less common)
        "healthy": 0.59      # Remaining chance of being healthy (no specific disease)
    }

    # 2. Define Likelihoods (P(Symptom|Disease))
    # These are conditional probabilities. In a real system, these would come from
    # medical research and clinical studies.
    likelihoods = {
        "flu": {
            "fever": 0.9,
            "cough": 0.8,
            "headache": 0.7,
            "sore throat": 0.6,
            "fatigue": 0.95,
            "sneezing": 0.2
        },
        "common cold": {
            "fever": 0.3,
            "cough": 0.9,
            "headache": 0.4,
            "sore throat": 0.8,
            "fatigue": 0.5,
            "sneezing": 0.9
        },
        "allergies": {
            "fever": 0.05,
            "cough": 0.3,
            "headache": 0.2,
            "sore throat": 0.1,
            "fatigue": 0.4,
            "sneezing": 0.95,
            "itchy eyes": 0.8
        },
        "pneumonia": {
            "fever": 0.95,
            "cough": 0.9,
            "headache": 0.5,
            "sore throat": 0.3,
            "fatigue": 0.8,
            "shortness of breath": 0.7,
            "chest pain": 0.6
        },
        "healthy": { # Assuming minimal or no symptoms if healthy
            "fever": 0.01,
            "cough": 0.05,
            "headache": 0.05,
            "sore throat": 0.02,
            "fatigue": 0.1,
            "sneezing": 0.05
        }
    }

    # Extract all unique symptoms for user input validation
    available_symptoms = set()
    for disease_likelihoods in likelihoods.values():
        available_symptoms.update(disease_likelihoods.keys())
    available_symptoms = sorted(list(available_symptoms)) # Sort for consistent display

    while True:
        observed_symptoms = get_user_symptoms(available_symptoms)

        if not observed_symptoms:
            print("\nNo symptoms entered. Assuming healthy or no specific diagnosis.")
            # If no symptoms, posterior probabilities should just be the priors
            for disease, prob in sorted(priors.items()):
                print(f"Probability of {disease.replace('_', ' ').title()}: {prob:.2%}")
        else:
            posterior_probabilities = calculate_posterior(priors, likelihoods, observed_symptoms)

            print("\n--- Diagnosis Results (Posterior Probabilities) ---")
            sorted_results = sorted(posterior_probabilities.items(), key=lambda item: item[1], reverse=True)
            for disease, prob in sorted_results:
                print(f"Probability of {disease.replace('_', ' ').title()}: {prob:.2%}")
            print("-------------------------------------------------")

        another_diagnosis = input("\nDo you want to perform another diagnosis? (yes/no): ").strip().lower()
        if another_diagnosis != 'yes':
            print("Thank you for using the Bayesian Medical Diagnosis System!")
            break

if __name__ == "__main__":
    main()