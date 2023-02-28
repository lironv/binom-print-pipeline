pipeline {
    agent any

    stages {
        stage('Execute Newton binom') {
            steps {
                sh 'python binom.py ${params.num}'
            }
        }
    }

    parameters {
        string(name: 'num', defaultValue: '10', description: 'Enter a number for Newton binomial calculation')
    }

    post {
        always {
            archiveArtifacts artifacts: '**', fingerprint: true
        }
    }
}
