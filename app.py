import os

import openai
from flask import Flask, redirect, render_template, request, url_for
import json

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prompt),
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", cards=response.choices[0].text))

    cards = json.loads(request.args.get("cards"))
    return render_template("index.html", cards=cards['flipCards'])


def generate_prompt(prompt):
    return """Prompt: Create 10 review questions about the French revolution with answers and refences?
Response:{{
"flipCards": [
{{
"question": "What was the main cause of the French Revolution?",
"answer": "The main cause was social and economic inequality between the wealthy and the poor, combined with a financial crisis in the country.",
"reference": "The French Revolution by William Doyle"
}},
{{
"question": "What was the main cause of the French Revolution?",
"answer": "The main cause was social and economic inequality between the wealthy and the poor, combined with a financial crisis in the country.",
"reference": "The French Revolution: A Very Short Introduction by Gary Kates"
}},
{{
"question": "Who was the leader of the French Revolution?",
"answer": "Maximilien Robespierre was one of the most influential leaders.",
"reference": "Robespierre: A Revolutionary Life by Lynn Hunt"
}},
{{
"question": "What was the outcome of the French Revolution?",
"answer": "The outcome was the establishment of the First French Republic, the execution of King Louis XVI, and the rise of Napoleon Bonaparte.",
"reference": "A People's History of the French Revolution by Stephane Courtois"
}},
{{
"question": "What was the role of the Third Estate in the French Revolution?",
"answer": "The Third Estate, representing common people, played a key role by demanding reforms and overthrowing the monarch.",
"reference": "The Third Estate in the French Revolution by Lynn Hunt"
}},
{{
"question": "What was the Reign of Terror in the French Revolution?",
"answer": "The Reign of Terror was a period of extreme violence characterized by mass executions.",
"reference": "The French Revolution: A Very Short Introduction by Gary Kates"
}},
{{
"question": "What was the Declaration of the Rights of Man and Citizen?",
"answer": "The Declaration proclaimed fundamental rights of all citizens including liberty, property, and equality before the law.",
"reference": "The French Revolution and Human Rights: A Brief Documentary History edited by Lynn Hunt"
}},
{{
"question": "Who were the Girondins and the Jacobins?",
"answer": "The Girondins advocated for a constitutional monarchy, the Jacobins for a republic.",
"reference": "N/A"
}}
]
}}
Prompt: {}
Response: """.format(prompt)
