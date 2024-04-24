# predict_customer_churn.py

def predict_churn(ann, sc):
    def get_user_input():
        print("Enter customer details to predict churn:")
        geography = input("Geography (France/Spain/Germany): ").strip()
        credit_score = float(input("Credit Score (350-850): "))
        gender = input("Gender (Male/Female): ").strip()
        age = int(input("Age: "))
        tenure = int(input("Tenure (years): "))
        balance = float(input("Balance: "))
        num_of_products = int(input("Number of Products: "))
        has_cr_card = int(input("Has Credit Card (1=Yes, 0=No): "))
        is_active_member = int(input("Is Active Member (1=Yes, 0=No): "))
        estimated_salary = float(input("Estimated Salary: "))
        
        # Convert inputs to match model's expected input format
        gender_encoded = 1 if gender.lower() == 'male' else 0
        geography_encoded = [0, 0, 0]
        if geography.lower() == 'spain':
            geography_encoded = [0, 1, 0]
        elif geography.lower() == 'germany':
            geography_encoded = [1, 0, 0]
        
        user_input = [geography_encoded + [credit_score, gender_encoded, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary]]
        return user_input
    
    user_input = get_user_input()
    user_input_scaled = sc.transform(user_input)
    prediction = ann.predict(user_input_scaled) > 0.5
    
    if prediction:
        print("The model predicts the customer will churn.")
    else:
        print("The model predicts the customer will not churn.")
