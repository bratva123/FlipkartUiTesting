pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'python -m pytest -s -v tests/**Test.py  --html=reports_and_log/report.html'
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
            emailext attachLog: true,attachmentsPattern: '**/reports_and_log/**.html', body: 'Hi \n Sending reports of testing',to:'suryakantsing890@gmail.com', subject: 'Test'
        }
    }
}
