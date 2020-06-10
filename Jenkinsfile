pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('CheckoutModule1') {
        steps {
            sh 'mkdir -p Module1'
            dir("Module1")
            {
                git branch: "master",
                url: 'https://github.com/bratva123/SeleniumWithPython.git'
            }
        }
    }
        
        stage('CheckoutModule2') {
        steps {
            sh 'mkdir -p Module2'
            dir("Module1")
            {
                git branch: "master",
                url: 'https://github.com/bratva123/Dummy.git'
            }
        }
    }
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'pip install pytest-cov'
                sh 'python -m pytest -s -v tests/login_tests.py tests/searchResultTest.py  --html=reports_and_log/report.html --cov=tests/'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
    post {
        always {
            emailext attachLog: true,attachmentsPattern: '**/reports_and_log/**.html,**/reports_and_log/**.log', body: 'Hi \n Sending reports of testing',to:'lavkr0403@gmail.com', subject: 'Test'
        }
    }
}
