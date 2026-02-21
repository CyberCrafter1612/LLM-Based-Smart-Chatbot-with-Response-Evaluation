import os
from openai import OpenAI
from evaluator import evaluate_response
from prompt_refiner import refine_prompt
from feedback_store import save_feedback

client = OpenAI(api_key="YOUR_API_KEY")

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def chatbot():
    print("🤖 Smart Chatbot Started (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Step 1: Generate response
        response = generate_response(user_input)
        print("\nBot:", response)

        # Step 2: Evaluate response
        scores = evaluate_response(user_input, response)
        print("\n📊 Evaluation:", scores)

        # Step 3: Improve if needed
        if scores["overall"] < 7:
            print("\n⚡ Improving response...")
            refined_prompt = refine_prompt(user_input)
            improved_response = generate_response(refined_prompt)

            print("\n✅ Improved Response:", improved_response)

            # Re-evaluate
            improved_scores = evaluate_response(user_input, improved_response)
            print("\n📊 Improved Evaluation:", improved_scores)

            final_response = improved_response
            final_scores = improved_scores
        else:
            final_response = response
            final_scores = scores

        # Step 4: Save feedback
        save_feedback(user_input, final_response, final_scores)

if __name__ == "__main__":
    chatbot()
