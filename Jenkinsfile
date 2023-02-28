pipeline {
    agent any
    
    stages {
       

        stage('Execute Newton binom') {
            steps {
                git branch: 'main', url: 'https://github.com/lironv/binom-print-pipeline.git'

                sh 'python binom.py ${params.num}'
            }
        }
    }

    parameters {
        string(name: 'num', defaultValue: '10', description: 'Enter a number for Newton binomial calculation')
    }

    
}
