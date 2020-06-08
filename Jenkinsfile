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
             emailext attachLog: true,attachmentsPattern: '**/reports_and_log/**.html,**/reports_and_log/**.log', body: 'Hi \n Sending reports of testing',to:'lavkr0403@gmail.com', subject: 'Test''
        }
    }
}
