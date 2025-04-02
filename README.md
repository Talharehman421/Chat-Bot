Here's a **README** file for your **chatbot script** using OpenAI's API.  

---

# **Chatbot Using OpenAI API**

This project is a **simple command-line chatbot** that interacts with users using OpenAI's **GPT-3.5-turbo** model.  

## **Features**
- Accepts user questions in an interactive loop.  
- Generates responses using OpenAI's chat completion API.  
- Keeps the conversation flowing dynamically.  

## **Prerequisites**
Ensure you have the following installed:  
- **Python 3.x**  
- **BoltIoT AI SDK** (`boltiotai`)  
- **OpenAI API Key**  

## **Installation & Setup**
1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Install dependencies:  
   ```sh
   pip install boltiotai
   ```
3. Set up your OpenAI API key as an environment variable:  
   ```sh
   export OPENAI_API_KEY='your-api-key-here'  # Linux/macOS
   set OPENAI_API_KEY='your-api-key-here'  # Windows (Command Prompt)
   ```

## **Usage**
Run the script with:  
```sh
python chat.py
```
Then, enter your questions when prompted. The chatbot will generate answers based on OpenAI's GPT-3.5-turbo.

## **Example Interaction**
```
Q: Who won the world series in 2020?
Ans: The Los Angeles Dodgers won the World Series in 2020.

Q: What is the capital of France?
Ans: The capital of France is Paris.
```

## **License**
This project is open-source and available under the MIT License.

## **Acknowledgments**
- Powered by [OpenAI](https://openai.com/)  
- Built using [BoltIoT AI SDK](https://www.boltiot.com/)  

---
