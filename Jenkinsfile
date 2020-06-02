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
            emailext (
                    subject: "Job '${env.JOB_NAME} ${env.BUILD_NUMBER}'",
                    body: """<p>Check console output at <a href="${env.BUILD_URL}">${env.JOB_NAME}</a></p>""",
                    to: "suryakantsingh890@gmail.com",
                    from: [[$class: 'DevelopersRecipientProvider']]
                  )
        }
    }
}
