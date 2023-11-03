# backstage-challenge-dockerized
This project is a dockerized version of the backstage technical challenge

### Local setup
1. `git clone git@github.com:zachcalvert/backstage-challenge.git`
2. `cd backstage-challenge`
3. `docker compose build`
4. `docker compose run --rm manage migrate`
5. `docker compose up`

- The react client will be available at: http://localhost:3000/
- The difference endpoint is available at: http://localhost:8000/api/difference?number=10  
- The pythagorean triplet endpoint is available at: http://localhost:8000/api/pythagorean_triplet?a=3&b=4&c=5


### Running the tests
1. `docker compose run --rm manage test`
