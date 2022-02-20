Error on Purpose
pipeline {
  agent any
  stages {
    stage("Clone") {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], 
        extensions: [], 
        userRemoteConfigs: [[url: 'https://github.com/vbalabin/jenkins_test']]])   	   
      }
    }
    stage("Build image") {
      steps {
        catchError {
          script {
            docker.build("python-web-tests", "-f Dockerfile .")
          }
        }
        stash name:'all', includes:'**'
      }
    }
    stage('Run tests') {
      agent {
        docker {
            image 'python-web-tests'
            args '--network host'
        }
      }
      steps {
        unstash 'all'
        sh '''
          pytest --disable-pytest-warnings --alluredir=target/allure-results ./tests
        '''
        sh 'pwd'
        sh 'ls'
        stash name:'results', includes:'**'
      }
    }
    stage('Build report'){
        steps{
          unstash 'results'
          allure includeProperties: false, jdk: '', results: [[path: 'target/allure-results']]
        }
    }
  }
}
