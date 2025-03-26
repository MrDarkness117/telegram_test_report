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
                sh 'pytest --html=reports/report.html --alluredir=allure-results --self-contained-html --maxfail=1 --disable-warnings --tb=short'
            }
        }
        stage('Publish Report') {
            steps {
                piblishHTML (target: [
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