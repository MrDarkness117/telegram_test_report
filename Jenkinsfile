pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/MrDarkness117/telegram_test_report.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings --tb=short'
            }
        }
    }
}