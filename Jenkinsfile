pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/lironv/binom-print-pipeline.git'
            }
        }

        stage('Execute Newton binom') {
            steps {
                sh 'python binom.py ${params.num}'
            }
        }
    }

    parameters {
        string(name: 'num', defaultValue: '10', description: 'Enter a number for Newton binomial calculation')
    }

    
}
