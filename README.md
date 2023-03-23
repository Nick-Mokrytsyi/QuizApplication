# Django QUIZ

[![Testing](https://github.com/Nick-Mokrytsyi/QuizApplication/actions/workflows/Test.yml/badge.svg)](https://github.com/Nick-Mokrytsyi/QuizApplication/actions/workflows/Test.yml)

## Technical requirements
### Web-UI
  1. Registration
      - [x] Registration (with email confirmation)
      - [x] Authorization
      - [x] Password change
      - [x] Password reset
    
  2. User capabilities
      - [x] Passing any test
      - [x] Sequentially answering test questions (one after another)
      - [x] Finishing a deferred test
      - [x] Removing an unfinished test
      - [x] Viewing results
    
  3. After completing a test
      - [x] Report on the number of correct and incorrect answers
      - [x] Percentage of correct answers

### Admin site
  1. [x] User management
  2. [ ] Test management
      - [x] Adding a test
      - [x] Modifying a test
      - [x] Deleting a test
      - [x] Test validation
        - [x] Can't save the question:
            - [x] without indicating the correct answer
            - [x] where all answers are correct
        - [ ] Can't save the test if:
            - [x] incorrect order_num (should be from 1 to 100 and increase by 1)
            - [x] the max value of order_num isn't more than the max allowable number of questions
            - [x] the number of questions is less than 3 or more than 100

### Additional requirements
1. [x] The project must be on Git
2. [x] requirements.txt file
3. [x] venv
4. [x] PostgresSQL
5. [x] The presence of a data dump
6. [x] Bootstrap
7. [x] Unit Tests
8. [ ] Docker image
9. [ ] Deployment on Amazon
10. [ ] Scheduler
11. [ ] Caching



ext.: [ ] API + Tests

