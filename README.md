[Test Plan](https://docs.google.com/document/d/1qplmZWMLb8_eu07okn77_JtG1IinPSc0_xjxANsrLas/edit?pli=1#heading=h.uwnx6qo5hm3c), see Sections Starting with *

To run

UI: 
* in `/scripts` run `locust`
* Navigate to http://localhost:8089/
* Provide number of locusts (users), spawn rate, and base url

CMD
* in `/scripts`
* Run `locust -f .\LurkersUsers.py --host https://jsonplaceholder.typicode.com --users 5
  --spawn-rate 1 --run-time 5m --headless`