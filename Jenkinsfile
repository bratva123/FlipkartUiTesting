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
                sh 'python -m pytest -s -v tests/login_tests.py tests/searchResultTest.py  --html=reports_and_log/report.html'
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
            emailext attachLog: true,attachmentsPattern: '**/reports_and_log/**.html', body: 'Hi \n Sending reports of testing', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
            mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: 'lavkr0403@gmail.com', mimeType: 'text/html', replyTo: 'suryakantsingh890@gmail.com', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "suryakantsingh890@foomail.com";
        }
    }
}
