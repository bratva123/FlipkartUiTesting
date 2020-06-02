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
            mail(
        bcc: '',
        body: "<p>your body</p>",
        cc: '',
        charset: 'UTF-8',
        from: '',
        mimeType: 'text/html',
        replyTo: '',
        subject: "your subject",
        to: "suryakantsingh890@gmail.com"
)
        }
    }
}
