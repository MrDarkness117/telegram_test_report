pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MrDarkness117/telegram_test_report.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install python3-venv'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest --html=reports/report.html --alluredir=allure-results --self-contained-html --maxfail=1 --disable-warnings --tb=short'
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML (target: [
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'PyTest HTML Report',
                    keepAll: true
                ])
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results -o allure-report --clean'
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure([
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}