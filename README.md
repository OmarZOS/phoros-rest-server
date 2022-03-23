# Social data provisioning server

 This repository holds the component that wraps the phoros project as a REST service.

## Getting started:

#### Dependencies:

##### - [Extractor](https://github.com/OmarZOS/remote-extraction-proxy-and-worker):

##### - [Storage](https://github.com/OmarZOS/social-graph-storage):

##### - [Transformer](https://github.com/OmarZOS/data-transformation-reverse-proxy):

#### Installing:

    docker-compose up -d

#### Debugging:

Open your browser (from your localhost) at: 
[http://localhost:2018/docs](http://localhost:2018/docs)



## Progress:

 - [ ] Handling requests. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/80)
   - [x] Wrapper files.
 - [ ] Wrapping. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
   - [ ] Extractor.
   - [ ] Transformer.
   - [ ] Storage.
 - [ ] Current code consistency. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/69)
   - [x] Listening to data providers.
     - Rabbitmq.
   - [ ] Serving data.
     - [x] Basic server functionality.
     - [ ] Advanced query handling.
 - [x] Containerisation ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
   - [x] Light footprint.
   - [x] Automation of deployment.

---
**NOTE** 

  -  On Ubuntu 20.04, containers have some problems with the firewall policies. [[Potential solution](https://stackoverflow.com/questions/30383845/what-is-the-best-practice-of-docker-ufw-under-ubuntu)]

---

