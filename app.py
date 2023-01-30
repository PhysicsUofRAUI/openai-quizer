import os

import openai
from flask import Flask, redirect, render_template, request, url_for

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
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(prompt):
    return """Prompt: Create 10 review questions about the French revolution with answers and refences?
Response:<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the main cause of the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>The main cause of the French Revolution was social and economic inequality between the wealthy and the poor, combined with a financial crisis in the country.</p>
      <p>Reference: "The French Revolution" by William Doyle.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the main cause of the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>The main cause of the French Revolution was social and economic inequality between the wealthy and the poor, combined with a financial crisis in the country.</p>
      <p>Reference: "The French Revolution: A Very Short Introduction" by Gary Kates</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>Who was the leader of the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>Maximilien Robespierre was one of the most influential leaders of the French Revolution.</p>
      <p>Reference: "Robespierre: A Revolutionary Life" by Lynn Hunt.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the outcome of the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>The outcome of the French Revolution was the establishment of the First French Republic, the execution of King Louis XVI, and the rise of Napoleon Bonaparte.</p>
      <p>Reference: "A People's History of the French Revolution" by Stephane Courtois.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the role of the Third Estate in the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>The Third Estate, which represented the common people of France, played a key role in the French Revolution by demanding political and economic reforms and ultimately overthrowing the monarch</p>
      <p>Reference: "The Third Estate in the French Revolution" by Lynn Hunt.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the Reign of Terror in the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>The Reign of Terror was a period of extreme violence during the French Revolution, characterized by mass executions of perceived enemies of the revolution.</p>
      <p>Reference: "The French Revolution: A Very Short Introduction" by Gary Kates.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the Declaration of the Rights of Man and Citizen?</p>
    </div>
    <div class="flip-card-back">
      <p>The Declaration of the Rights of Man and Citizen was a document adopted during the French Revolution that proclaimed the fundamental rights of all citizens, including liberty, property, and equality before the law.</p>
      <p>Reference: "The French Revolution and Human Rights: A Brief Documentary History" edited by Lynn Hunt.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>Who were the Girondins and the Jacobins?</p>
    </div>
    <div class="flip-card-back">
      <p>The Girondins were a political group that emerged during the French Revolution and advocated for a constitutional monarchy, while the Jacobins were a more radical group that sought a democratic and secular republic.</p>
      <p>Reference: "The Political Culture of the French Revolution" by Bryant T. Ragan Jr.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the role of women in the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>Women played a significant role in the French Revolution by participating in political demonstrations, forming their own political organizations, and pushing for women's rights.</p>
      <p>Reference: "The Women's Revolution in France, 1789-1796" by Darline Gay Levy.</p>
    </div>
  </div>
</div>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p>What was the role of the Enlightenment in the French Revolution?</p>
    </div>
    <div class="flip-card-back">
      <p>The Enlightenment, with its emphasis on reason, science, and individual rights, provided a philosophical foundation for the French Revolution and influenced its ideas and ideals.</p>
      <p>Reference: "The French Revolution and the Enlightenment" edited by Daniel L. Schlafly Jr.</p>
    </div>
  </div>
</div>
Prompt: {}
Response:""".format(prompt)
