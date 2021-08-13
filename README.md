<h1 align="center">
  <img src="logo.gif" alt="CertGen" width="512">
</h1>

## Demo Video
<div align="center">
  <a href="https://www.youtube.com/watch?v=8DUY9tWg95M">
    <img src="https://img.youtube.com/vi/8DUY9tWg95M/0.jpg" width="75%">
  </a>
</div>


## Inspiration ❗💡

> "Why spend 5 minutes doing a menial task when you can spend 10 hours failing to automate it? 😂"

(Spoiler Alert: We actually succeeded! :P)

In the last year-and-half spent in this upside-down pandemic-ruled world, the only way we've been able to organize and conduct hackathons and other events is digital.

With digital events taking over the entire segment, it brings along with it the challenge that everyone wants digital certificates now too. 

And in this, we saw a problem statement that we could solve, one that we could automate with code.

That's exactly what we did! ;)


## What does it do ❓
This web app and CLI tool (However you choose to roll ;)) automagically grabs participant info from google sheets and generates certificates using Flask and Python, stores them in AstraDB, and emails them to the participants via the Twilio Sendgrid API!


## How we built it 💻🔧🔨🧰

- Most events tend to run their operations out of **Google Sheets**, so we chose to write a **Google App Script** to hit the **Certificate Generator API** with the data stored in the spreadsheets.
- We wrote the **Certificate Generator API** in **Python & Flask** and hosted it on **Linode Cloud**.
- We used **DataStax Astra's AstraDB** hosted on **Google Cloud Platform** to store the generated certificates for a certain period of time in case a participant wanted a copy of their certificates.
-  We used the **Twilio Sendgrid API** to email participants their certificates once they were successfully generated.


## Challenges we ran into  🏃‍♂️❌

It was our first time deploying on Google Cloud and using Datastax Astra, and two of our team members have never used Flask before.
It was an amazing learning experience, albeit a little painful :P


## Accomplishments that we're proud of 🏆🏅

- **Our team consists of 50% hackers that are very new to the game**
- **We learned to use and deploy on Google Cloud for the first time!**
- **We used Datastax Astra and Twilio SendGrid for the first time!**
- **All of us learned something about the tech that we used for the first time**
- **We met some really cool people and had lots of fun in the hacker hangouts and mini-events.**


## What we learned 🧠

- **Prototyping and Designing in Figma**
  Figma is a browser-based UI and UX design application and was recommended by a teammate. So one of us used Figma, switching from Photoshop for the first time. We eventually did get the hang of it, though, and could easily craft neat UIs.

- **Building Flask Apps**
  Flask is an open-source Python library used for developing APIs. This was the first time we worked with Flask as well as creating an end-to-end web application. And it was a wonderful opportunity to learn and figure out how things work in web applications. From having always admired beautiful web pages to going ahead and actually building something for MLH was a wonderful experience!

- **Using Datastax Astra to setup distributed CQL databases on Google Cloud Platform**

- **Using Linode to host our Flask Backend**

- **One of our team members automated a process and learned to use Git for the time.**


## What's next for CertGen ⏭
We're looking to do a public rollout and add more templates for certificates.