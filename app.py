from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

@app.route('/download-resume')
def download_resume():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'Dhanush_Kumar_Reddy_Yarragonda_resume.pdf', as_attachment=True)

# Main page
@app.route('/')
def home():
    portfolio_data = {
        "name": "YARRAGONDA DHANUSH KUMAR REDDY",
        "title": "Software Developer",
        "about": "I'm Dhanush Kumar Reddy Yarragonda, a passionate software developer with a strong foundation in Python programming and hands-on experience in DevOps tools and cloud platforms like AWS, Azure, and GCP. I enjoy building efficient backend systems, automating workflows, and deploying scalable cloud-native applications. With a background in Computer Science and a focus on continuous learning, I'm committed to solving real-world problems through clean code and modern DevOps practices.", 
        "background_video": "background.mp4",
        "education": [
            {
                "university": "University at Buffalo",
                "degree": "Master of Science in Computer Science",
                "location": "Buffalo, NY",
                "relevant_courses": [
                    "Reinforcement Learning",
                    "Data Structures",
                    "Algorithms",
                    "Machine Learning",
                    "Deep Learning",
                    "Data Intensive Computing"
                ]
            },
            {
                "university": "Vellore Institute of Technology",
                "degree": "Bachelor's in Electronics and Communication Engineering",
                "location": "Vellore, India"
            }
        ],
        "skills": {
            "Languages": ["Python", "Shell Scripting", "SQL", "YAML", "HTML"],
            "Developer Tools": ["Git", "GitHub", "VS Code", "Docker CLI"],
            "Technologies/Frameworks": ["Flask", "Django", "AWS", "Azure", "GCP"]
        },
        "projects": [
            {
                "name": "EMOTION RECOGNITION FROM FACIAL EXPRESSIONS",
                "description": [
                    "Collaborated with a team to Train a deep learning model to recognize human emotions based on facial expressions. This can be used in a range of applications from user interface design to mental health monitoring",
                    "Evaluation of six distinct models including Basic CNN, Simple ResNet, Variation of GoogleNet, UNet (Encoder and Decoder), NewNet, and RogleNet.",
                    "Implementation of innovative techniques such as data augmentation, weighted cross-entropy loss, and optimization algorithms like SGD and Adam for enhanced model performance"
                ]
            },
            {
                "name": "DEEP REINFORCEMENT ALGORITHMS",
                "description": [
                    "Implemented Deep Q-Networks (DQN), Double DQN (DDQN), Actor Critic, advantage Actor Critic Algorithms to solve custom multiAgent environments such as Tic-Tac-Toe, Rock Paper Scissors and Switch Game.",
                    "Built a custom model using innovative techniques like experience relay methods, enhancing performance of existing algorithm, achieving over 92% accuracy"
                ]
            }
        ],
        "experience": [
            {
                "company": "SIRI SOLUTIONS INC",
                "position": "SOFTWARE DEVELOPER",
                "details": [
                    "Designed and deployed scalable backend modules using Python on cloud-hosted servers (AWS EC2).",
                    "Automated routine tasks and deployment processes with custom Python and shell scripts, reducing manual effort by 60%.",
                    "Built REST API integrations and automated testing using Postman and Python scripts.",
                    "Contributed to infrastructure automation using Git and Docker for consistent environment setup."
                ]
            },
            {
                "company": "SACRO",
                "position": "PYTHON DEVELOPER INTERN",
                "details": [
                    "Developed and automated data processing pipelines using Python, improving reporting efficiency by 40%.",
                    "Implemented unit tests using pytest, increasing code reliability and test coverage.",
                    "Optimized scripts and integrated logging to enhance monitoring and reduce runtime errors.",
                    "Introduced basic CI workflows using Git and GitHub Actions for testing automation."
                ]
            }
        ],
        "contact": {
            "email": "dhanushkumarreddy0514@gmail.com",
            "linkedin": "www.linkedin.com/in/dkry",
            "phone": "+919441572688"
        }
    }
    return render_template('index.html', data=portfolio_data)

# Dedicated pages for each section
@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/education')
def education_page():
    return render_template('education.html')

@app.route('/skills')
def skills_page():
    return render_template('skills.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html')

@app.route('/experience')
def experience_page():
    return render_template('experience.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)