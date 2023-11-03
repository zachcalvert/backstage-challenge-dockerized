# backstage-challenge-dockerized
This project is a dockerized version of the backstage technical challenge

### Local setup
1. `git clone git@github.com:zachcalvert/backstage-challenge-dockerized.git`
2. `cd backstage-challenge-dockerized`
3. `docker compose run --rm manage migrate`
4. `docker compose up --build`

- The react client will be available at: http://localhost:3000/
- The difference endpoint is available at: http://localhost:8000/api/difference?number=10  
- The pythagorean triplet endpoint is available at: http://localhost:8000/api/pythagorean_triplet?a=3&b=4&c=5

### Running the tests
1. `docker compose run --rm manage test`

### Teardown
You can remove artifacts from running this project with `docker compose down --rmi all` 

