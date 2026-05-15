from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    name = request.form['name']
    interest = request.form['interest']
    skills = request.form['skills']
    cgpa = request.form['cgpa']

    interest_lower = interest.lower()

    if "ai" in interest_lower or "machine learning" in interest_lower:
        career = "AI Engineer"
        roadmap = [
            "Learn Python",
            "Learn Machine Learning",
            "Learn Deep Learning",
            "Learn TensorFlow or PyTorch",
            "Build AI Projects",
            "Create GitHub Portfolio"
        ]

    elif "web" in interest_lower:
        career = "Full Stack Web Developer"
        roadmap = [
            "Learn HTML",
            "Learn CSS",
            "Learn JavaScript",
            "Learn React",
            "Learn Backend Development",
            "Build Full Stack Projects"
        ]

    elif "cyber" in interest_lower or "security" in interest_lower:
        career = "Cybersecurity Engineer"
        roadmap = [
            "Learn Networking Basics",
            "Learn Linux",
            "Study Ethical Hacking",
            "Practice Cybersecurity Tools",
            "Do Security Projects",
            "Prepare for Certifications"
        ]

    elif "data" in interest_lower:
        career = "Data Scientist"
        roadmap = [
            "Learn Python",
            "Learn Data Analysis",
            "Learn Pandas and NumPy",
            "Study Machine Learning",
            "Build Data Projects",
            "Practice Visualization"
        ]

    else:
        career = "Software Developer"
        roadmap = [
            "Learn Programming Fundamentals",
            "Practice Python or Java",
            "Learn Problem Solving",
            "Build Mini Projects",
            "Learn Databases",
            "Create Resume and Portfolio"
        ]

    return render_template(
        'index.html',
        name=name,
        career=career,
        roadmap=roadmap,
        skills=skills,
        cgpa=cgpa
    )


if __name__ == '__main__':
    app.run(debug=True)