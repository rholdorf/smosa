# 🗺️ Subway Map of Software Architecture (SMoSA)

The **Subway Map of Software Architecture (SMoSA)** is a **visual knowledge framework** designed to represent the complex ecosystem of software architecture concepts, practices, and decisions through the metaphor of a **metro map**.  
Each **line** represents a thematic domain of architectural knowledge (e.g., *Quality Attributes, Architectural Styles, DevOps, Security*), and each **station** represents a key concept, pattern, or reference from the literature.

SMoSA aims to **connect theoretical foundations, modern practices, and empirical insights** in a cohesive and intuitive structure to support **architectural learning, assessment, and communication**.

![Subway Map of Software Architecture](./subwaymap.png)
---

## 🎯 Purpose

- To provide a **visual taxonomy** of the main areas of software architecture.
- To bridge **academic and industrial perspectives** on architectural practices.
- To serve as the conceptual foundation for **architecture maturity assessments** and **visual dashboards** such as those in the current PhD Reseach of Manoel Valerio da Silveira Neto.
- To promote **continuous architectural reflection** in agile and DevOps environments.

---

## 🧠 Conceptual Background

SMoSA was developed in the context of doctoral research on **software architecture evaluation in agile environments**, integrating:
- **ISO/IEC 25010:2023** Quality Attributes  
- **Architecture Evaluation Methods** (ATAM, SAAM, CBAM, ALMA)  
- **Agile and DevOps Practices**  
- **Architecture Decision Records (ADRs)**  
- **Modern Paradigms** such as *Evolutionary Architecture, Microservices, Cloud-Native Design*, and *Continuous Architecture*.

It aligns with well-known references such as:
- Bass, Clements, and Kazman — *Software Architecture in Practice*  
- Ford, Parsons, and Kua — *Building Evolutionary Architectures*  
- Richards and Ford — *Fundamentals of Software Architecture*  
- ISO/IEC/IEEE 42010 — *Architecture Description*  

---

## 🚀 Applications

- **Educational Tool**: Used in software architecture courses to teach interrelated topics.  
- **Research Artifact**: Forms the basis for the *Agile Software Architecture Assessment Framework (ASAAF)*.  
- **Organizational Use**: Can guide architecture reviews, roadmaps, and knowledge sharing within teams.  
- **Visualization Dashboard**: Integrates with radar charts and maturity tables for architectural assessments.

---

## 📚 Citation

If you use SMoSA in your work, please cite:

> Silveira Neto, M. V. da; Malucelli, A.; Reinehr, S.  
> **"Subway Map of Software Architecture (SMoSA): A Visual Framework for Architectural Knowledge and Maturity Assessment."**  
> Doctoral Research, PUCPR, 2025.

---

## 📄 License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license —  
you are free to share and adapt the material as long as proper credit is given.

---

## 🌐 Learn More


> *“The Subway Map is not just a visualization — it’s a shared mental model for architectural thinking, enabling continuous reflection, decision transparency, and evolution.”*

---

## 🧩 Structure

The SMoSA is organized into **10 main lines** (in current view), each containing multiple stations.  
Below are examples of lines and corresponding stations:

| Line | Description |
|------|--------------|
| **Strategic Principles and Decisions** | Covers the principles, philosophies, and critical decisions that form the foundation for creating and evolving a high-quality software architecture. |
| **Quality Attributes and Techniques** | Defines non-functional requirements and fundamental techniques to ensure that the architecture is robust, resilient, and efficient. |
| **Architectural Styles** | Presents high-level paradigms that define the structural organization of a system and how its main components interrelate. |
| **Architectural Patterns** | MVC, MVVM, API Gateway, Saga, Circuit Breaker, CQRS, Event Sourcing, Database per Service, Proxy Pattern |
| **Infraestructure and Distributed Architecture** | Addresses cloud service models and the inherent challenges of distributed systems, such as communication, data consistency, and service location. |
| **Data Architecture** | Focuses on patterns and styles related to data management, storage, processing, and flow at scale. |
| **Security Practices** | Covers essential practices, models, and technologies to integrate security into all architectural layers from the design stage. |
| **Agile and DevOps Practices** | Covers methodologies and processes that integrate Agile and DevOps principles to promote continuous delivery, automation, and architectural evolution. |
| **Architecture Documentation** | Presents methods, notations, and tools to effectively visualize, communicate, and record architectural decisions and structure for all stakeholders. |
| **Measurement and Evaluation** | Focuses on formal methods and techniques to objectively analyze, measure, and validate the quality and trade-offs of a software architecture. |


| Line Name | Station | Reference |
|------------|----------|------------|
| **Strategic Principles and Decisions** | Domain-Driven Design (DDD) | EVANS, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Boston: Addison-Wesley, 2003. |
| **Strategic Principles and Decisions** | API-First Design | GOUGH, James; BRYANT, Daniel; AUBURN, Matthew. *Mastering API Architecture: Design, Operate, and Evolve API-Based Systems.* Sebastopol: O’Reilly Media, 2022. |
| **Strategic Principles and Decisions** | Evolutionary Architecture | FORD, Neal; PARSONS, Rebecca; KUA, Patrick. *Building Evolutionary Architectures: Support Constant Change.* Sebastopol: O’Reilly Media, 2017. |
| **Strategic Principles and Decisions** | Legacy Modernization & Integration | NEWMAN, Sam. *Monolith to Microservices: Evolutionary Patterns to Transform Your Monolith.* Sebastopol: O’Reilly Media, 2019. |
| **Strategic Principles and Decisions** | SOLID, DRY, KISS, YAGNI | MARTIN, Robert C. *Clean Architecture: A Craftsman’s Guide to Software Structure and Design.* Boston: Prentice Hall, 2017. |
| **Strategic Principles and Decisions** | Separation of Concerns | PARNAS, David L. *On the Criteria to Be Used in Decomposing Systems into Modules.* *Communications of the ACM*, v. 15, n. 12, p. 1053–1058, 1972. |
| **Strategic Principles and Decisions** | High Cohesion & Low Coupling | BALDWIN, Carliss Y.; CLARK, Kim B. *Design Rules: The Power of Modularity.* Cambridge: MIT Press, 2000. |
| **Principles and Strategic Decisions** | Architectural Trade-offs | KAZMAN, Rick; KLEIN, Mark; CLEMENTS, Paul; et al. *The Architecture Tradeoff Analysis Method (ATAM): A Method for Evaluating Software Architectures.* Pittsburgh: Carnegie Mellon University, Software Engineering Institute, 2000. (CMU/SEI-2000-TR-004). |
| **Quality Attributes and Techniques** | Availability | ISO/IEC 25010:2023 – *Systems and Software Quality Requirements and Evaluation (SQuaRE) – System and Software Quality Models.* Geneva: ISO, 2023. |
| **Quality Attributes and Techniques** | Performance | ISO/IEC 25010:2023 – *Systems and Software Quality Requirements and Evaluation (SQuaRE) – System and Software Quality Models.* Geneva: ISO, 2023. |
| **Quality Attributes and Techniques** | Security | ISO/IEC 25010:2023 – *Systems and Software Quality Requirements and Evaluation (SQuaRE) – System and Software Quality Models.* Geneva: ISO, 2023. |
| **Quality Attributes and Techniques** | Scalability | GORTON, Ian. *Foundations of Scalable Systems: Designing Distributed Architectures.* Sebastopol: O’Reilly Media, 2022. |
| **Quality Attributes and Techniques** | Maintainability | ISO/IEC 25010:2023 – *Systems and Software Quality Requirements and Evaluation (SQuaRE) – System and Software Quality Models.* Geneva: ISO, 2023. |
| **Quality Attributes and Techniques** | Usability | ISO/IEC 25010:2023 – *Systems and Software Quality Requirements and Evaluation (SQuaRE) – System and Software Quality Models.* Geneva: ISO, 2023. |
| **Quality Attributes and Techniques** | Portability | ISO/IEC 25010:2023 – *Systems and Software Quality Requirements and Evaluation (SQuaRE) – System and Software Quality Models.* Geneva: ISO, 2023. |
| **Quality Attributes and Techniques** | Load Balancing | DAVIS, Cornelia. *Cloud Native Patterns: Designing Change-tolerant Software.* Shelter Island: Manning Publications, 2019. |
| **Quality Attributes and Techniques** | Redundancy & Failover | BEYER, Betsy et al. *Site Reliability Engineering: How Google Runs Production Systems.* Sebastopol: O’Reilly Media, 2016. |
| **Quality Attributes and Techniques** | Disaster Recovery | HEWITT, Eben. *Technology Strategy Patterns: Architecture as Strategy.* Sebastopol: O’Reilly Media, 2018. |
| **Quality Attributes and Techniques** | Partitioning/Sharding | KLEPPMANN, Martin. *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems.* Sebastopol: O’Reilly Media, 2017. |
| **Architectural Styles** | Monolithic | NEWMAN, Sam. *Monolith to Microservices: Evolutionary Patterns to Transform Your Monolith.* Sebastopol: O’Reilly Media, 2019. |
| **Architectural Styles** | Layered | RICHARDS, Mark. *Software Architecture Patterns.* Sebastopol: O’Reilly Media, 2015. |
| **Architectural Styles** | Microservices | NEWMAN, Sam. *Building Microservices: Designing Fine-Grained Systems.* 2nd ed. Sebastopol: O’Reilly Media, 2021. |
| **Architectural Styles** | Event-Driven Architecture (EDA) | STOPFORD, Ben. *Designing Event-Driven Systems: Concepts and Patterns for Streaming Services with Apache Kafka.* Sebastopol: O’Reilly Media, 2018. |
| **Architectural Styles** | Service-Oriented Architecture (SOA) | ERL, Thomas. *Service-Oriented Architecture: Concepts, Technology, and Design.* Upper Saddle River: Prentice Hall, 2005. |
| **Architectural Styles** | Hexagonal | COCKBURN, Alistair. *The Hexagonal Architecture.* 2005. Available at: https://alistair.cockburn.us/hexagonal-architecture/ |
| **Architectural Styles** | Serverless | SBARSKI, Peter. *Serverless Architectures on AWS: With Examples Using AWS Lambda.* Shelter Island: Manning Publications, 2017. |
| **Architectural Styles** | Clean Architecture | MARTIN, Robert C. *Clean Architecture: A Craftsman’s Guide to Software Structure and Design.* Boston: Prentice Hall, 2017. |
| **Architectural Styles** | BFF | NEWMAN, Sam. *Building Microservices: Designing Fine-Grained Systems.* 2nd ed. Sebastopol: O’Reilly Media, 2021. |
| **Architectural Styles** | Micro Frontend | GEERS, Michael. *Micro Frontends in Action.* Shelter Island: Manning Publications, 2020. |
| **Architectural Styles** | MACH | MACH ALLIANCE. *What is MACH?* Available at: https://machalliance.org |
| **Architectural Patterns** | MVC | GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. *Design Patterns: Elements of Reusable Object-Oriented Software.* Boston: Addison-Wesley, 1994. |
| **Architectural Patterns** | MVVM | MICROSOFT. *The MVVM Pattern.* Available at: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/mvvm-overview |
| **Architectural Patterns** | API Gateway | NEWMAN, Sam. *Building Microservices: Designing Fine-Grained Systems.* 2nd ed. Sebastopol: O’Reilly Media, 2021. |
| **Architectural Patterns** | Saga | RICHARDSON, Chris. *Microservices Patterns: With Examples in Java.* Shelter Island: Manning Publications, 2018. |
| **Architectural Patterns** | Circuit Breaker | NYGARD, Michael T. *Release It!: Design and Deploy Production-Ready Software.* 2nd ed. Raleigh: Pragmatic Bookshelf, 2018. |
| **Architectural Patterns** | CQRS | MICROSOFT. *CQRS Pattern.* Microsoft Learn. Available at: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs |
| **Architectural Patterns** | Event Sourcing | EVANS, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Boston: Addison-Wesley, 2003. |
| **Architectural Patterns** | Proxy Pattern | LARMAN, Craig. *Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and Iterative Development.* 3rd ed. Upper Saddle River: Prentice Hall, 2004. |
| **Infraestructure and Distributed Architecture** | IaaS | ERL, Thomas; PUTTINI, Ricardo; MAHMOOD, Zaigham. *Cloud Computing: Concepts, Technology & Architecture.* Boston: Prentice Hall, 2013. |
| **Infraestructure and Distributed Architecture** | PaaS | ERL, Thomas; PUTTINI, Ricardo; MAHMOOD, Zaigham. *Cloud Computing: Concepts, Technology & Architecture.* Boston: Prentice Hall, 2013. |
| **Infraestructure and Distributed Architecture** | Multicloud | KAVIS, Michael J. *Architecting the Cloud: Design Decisions for Cloud Computing Service Models (SaaS, PaaS, and IaaS).* Hoboken: Wiley, 2014. |
| **Infraestructure and Distributed Architecture** | Edge Computing | CAO, Jie; ZHANG, Quan; SHI, Weisong. *Edge Computing: A Primer.* In: SHI, Weisong; DUSTDAR, Schahram. *Edge Computing: Models, Technologies and Applications.* Cham: Springer, 2019. p. 3–28. |
| **Infraestructure and Distributed Architecture** | Eventual Consistency | GILBERT, Seth; LYNCH, Nancy. *Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services.* *ACM SIGACT News*, v. 33, n. 2, p. 51–59, 2002. |
| **Infraestructure and Distributed Architecture** | Data Replication | KLEPPMANN, Martin. *Designing Data-Intensive Applications.* Sebastopol: O’Reilly Media, 2017. |
| **Infraestructure and Distributed Architecture** | Queuing Systems | KLEPPMANN, Martin. *Designing Data-Intensive Applications.* Sebastopol: O’Reilly Media, 2017. |
| **Infraestructure and Distributed Architecture** | Service Discovery | RICHARDSON, Chris. *Microservices Patterns: With Examples in Java.* Shelter Island: Manning Publications, 2018. |
| **Data Architecture** | Data Mesh | DEHGHANI, Zhamak. *Data Mesh: Delivering Data-Driven Value at Scale.* Sebastopol: O'Reilly Media, 2022. |
| **Data Architecture** | Data Lakes & Data Warehouses | KIMBALL, Ralph; ROSS, Margy. *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling.* 3rd ed. Hoboken: Wiley, 2013. |
| **Data Architecture** | Lambda Architecture | MARZ, Nathan; WARREN, James. *Big Data: Principles and Best Practices of Scalable Realtime Data Systems.* Shelter Island: Manning Publications, 2015. |
| **Data Architecture** | Real-Time Data Streaming | AKIDAU, Tyler; CHERNYAK, Slava; LAX, Reuven. *Streaming Systems: The What, Where, When, and How of Large-Scale Data Processing.* Sebastopol: O’Reilly Media, 2018. |
| **Data Architecture** | Change Data Capture (CDC) | KLEPPMANN, Martin. *Designing Data-Intensive Applications.* Sebastopol: O’Reilly Media, 2017. |
| **Data Architecture** | Data Governance | SEINER, Robert S. *Non-Invasive Data Governance: The Path of Least Resistance and Greatest Success.* Basking Ridge: Technics Publications, 2014. |
| **Data Architecture** | Data Quality | MCGILVRAY, Danette. *Executing Data Quality Projects: Ten Steps to Quality Data and Trusted Information.* Burlington: Morgan Kaufmann, 2008. |
| **Data Architecture** | ETL/ELT Processes | KIMBALL, Ralph; CASERTA, Joe. *The Data Warehouse ETL Toolkit: Practical Techniques for Extracting, Cleaning, Conforming, and Delivering Data.* Indianapolis: Wiley, 2004. |
| **Security Practices** | Secure by Design | JOHNSSON, Dan Bergh; DEOGUN, Daniel; SAWANO, Daniel. *Secure by Design.* Shelter Island: Manning Publications, 2020. |
| **Security Practices** | Zero Trust Architecture | NIST. *Zero Trust Architecture.* NIST SP 800-207. Gaithersburg: NIST, 2020. |
| **Security Practices** | Threat Modeling | SHOSTACK, Adam. *Threat Modeling: Designing for Security.* Indianapolis: Wiley, 2014. |
| **Security Practices** | OAuth & SSO Authentication | RICHER, Justin; SANSO, Antonio. *OAuth 2 in Action.* Shelter Island: Manning Publications, 2017. |
| **Security Practices** | API Security Practices | MADDEN, Neil. *API Security in Action.* Shelter Island: Manning Publications, 2020. |
| **Security Practices** | Container Security | MOUAT, Adrian. *Using Docker: Developing and Deploying Software with Containers.* Sebastopol: O’Reilly Media, 2015. |
| **Agile and DevOps Practices** | Continuous Integration (CI) | HUMBLE, Jez; FARLEY, David. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Boston: Addison-Wesley, 2010. |
| **Agile and DevOps Practices** | Continuous Delivery (CD) | HUMBLE, Jez; FARLEY, David. *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Boston: Addison-Wesley, 2010. |
| **Agile and DevOps Practices** | Infrastructure as Code (IaC) | MORRIS, Kief. *Infrastructure as Code: Dynamic Systems for the Cloud Age.* 2nd ed. Sebastopol: O’Reilly Media, 2021. |
| **Agile and DevOps Practices** | Observability & Monitoring | SRIDHARAN, Cindy. *Distributed Systems Observability.* Sebastopol: O’Reilly Media, 2018. |
| **Agile and DevOps Practices** | Configuration Management | LIMONCELLI, Thomas A.; HOGAN, Christina J.; CHALUP, Strata R. *The Practice of System and Network Administration.* 3rd ed. Boston: Addison-Wesley, 2016. |
| **Agile and DevOps Practices** | 12-Factor App | WIGGINS, Adam. *The Twelve-Factor App.* [S.l.]: Heroku, 2011. Available at: https://12factor.net/ |
| **Agile and DevOps Practices** | Architecture at Scale (SAFe, LeSS) | LEFFINGWELL, Dean; KNASTER, Richard; JEMILO, Drew. *SAFe® 6.0 Reference Guide: Scaled Agile Framework® for Lean Enterprises.* Boston: Addison-Wesley, 2023. |
| **Architecture Documentation** | ADRs (Architecture Decision Records) | CLEMENTS, Paul C. et al. *Documenting Software Architectures: Views and Beyond.* 2nd ed. Boston: Addison-Wesley, 2010. |
| **Architecture Documentation** | UML | BOOCH, Grady; RUMBAUGH, James; JACOBSON, Ivar. *The Unified Modeling Language User Guide.* 2nd ed. Boston: Addison-Wesley, 2005. |
| **Architecture Documentation** | Viewpoints & Perspectives (4+1) | KRUCHTEN, Philippe. *Architectural Blueprints—The “4+1” View Model of Software Architecture.* *IEEE Software*, v. 12, n. 6, p. 42–50, 1995. |
| **Architecture Documentation** | Event Storming | BRANDOLINI, Alberto. *Introducing EventStorming: An Act of Deliberate Collective Learning.* Milano: Leanpub, 2019. |
| **Measurement and Evaluation** | ATAM | BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. *The Architecture Tradeoff Analysis Method.* Pittsburgh: SEI, Carnegie Mellon University, 2001. |
| **Measurement and Evaluation** | SAAM | KAZMAN, Rick; ABOWD, Gregory; BASS, Len; CLEMENTS, Paul. *Scenario-Based Analysis of Software Architecture.* *IEEE Software*, 1996. |
| **Measurement and Evaluation** | ALMA | BENGTSSON, P.; LASSING, N.; BOSCH, J.; VAN VLIET, H. *Architecture-Level Modifiability Analysis (ALMA).* *Journal of Systems and Software*, v. 69, n. 1–2, p. 129–147, 2004. |
| **Measurement and Evaluation** | AHP | SAATY, Thomas L. *The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation.* New York: McGraw-Hill, 1980. |
| **Measurement and Evaluation** | Architectural Quality Evaluation | KAZMAN, Rick; KLEIN, Mark H.; CLEMENTS, Paul. *Evaluating Software Architectures: Methods and Case Studies.* Boston: Addison-Wesley, 2002. |
| **Measurement and Evaluation** | Quality Attribute Measurement | KAZMAN, Rick; KLEIN, Mark H.; CLEMENTS, Paul. *Evaluating Software Architectures: Methods and Case Studies.* Boston: Addison-Wesley, 2002. |

 **Table Metrics** summarizes these indicative metrics for all analyzed sources. All citation counts and platform-based metrics were collected on December,~2025, and should therefore be interpreted as a temporal snapshot intended to support recurrence and visibility analysis rather than as stable bibliometric measures.
| {Source ID | Metric | Platform | Type | Amazon Rating  | Amazon Evaluations |
|--------------------|-----------------|-------------------|---------------|--------------------------|-----------------------------|
| S1                 | 2918            | Google Scholar    | Citation      | 4.6                      | 1486                        |
| S2                 | 41              | Google Scholar    | Citation      | 4.4                      | 32                          |
| S3                 | 148             | Google Scholar    | Citation      | 4.3                      | 341                         |
| S4                 | 452             | Google Scholar    | Citation      | 4.6                      | 626                         |
| S5                 | 1241            | Google Scholar    | Citation      | 4.7                      | 3923                        |
| S6                 | 8032            | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S7                 | 7775            | Google Scholar    | Citation      | 4.8                      | 5                           |
| S8                 | 983             | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S9                 | 15              | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S10                | 28              | Google Scholar    | Citation      | 4.5                      | 29                          |
| S11                | 61              | Google Scholar    | Citation      | 4.3                      | 41                          |
| S12                | 722             | Google Scholar    | Citation      | 4.6                      | 1181                        |
| S13                | 15              | Google Scholar    | Citation      | 4.3                      | 239                         |
| S14                | 1072            | Google Scholar    | Citation      | 4.8                      | 5300                        |
| S15                | 67              | ACM DL            | Citation      | N/A (not sold on Amazon) | N/A (not sold on Amazon)    |
| S16                | 4316            | Google Scholar    | Citation      | 4.7                      | 778                         |
| S17                | 108             | Google Scholar    | Citation      | 4.5                      | 8                           |
| S18                | 1378            | Google Scholar    | Citation      | 4.3                      | 58                          |
| S19                | 100             | Google Scholar    | Citation      | 4.8                      | 43                          |
| S20                | 156             | Google Scholar    | Citation      | 4.2                      | 70                          |
| S21                | 89              | Google Scholar    | Citation      | 4.2                      | 41                          |
| S22                | 23000           | LinkedIn          | Followers     | N/A (non-book)           | N/A (non-book)              |
| S23                | 23              | Google Scholar    | Citation      | 4.7                      | 2506                        |
| S24                | N/A             | --                | --            | N/A (non-book)           | N/A (non-book)              |
| S25                | 45              | Google Scholar    | Citation      | 4.6                      | 675                         |
| S26                | 326             | Google Scholar    | Citation      | 4.7                      | 497                         |
| S27                | 947             | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S28                | 947             | Google Scholar    | Citation      | 4.8                      | 56                          |
| S29                | 936             | Google Scholar    | Citation      | 4.4                      | 407                         |
| S30                | 2               | Google Scholar    | Citation      | 4.4                      | 177                         |
| S31                | 76              | Google Scholar    | Citation      | N/A (not sold on Amazon) | N/A (not sold on Amazon)    |
| S32                | 1059            | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S33                | 272             | Google Scholar    | Citation      | 4.7                      | 346                         |
| S34                | 7708            | Google Scholar    | Citation      | 4.6                      | 731                         |
| S35                | 2077            | Google Scholar    | Citation      | 4.2                      | 88                          |
| S36                | 147             | Google Scholar    | Citation      | 4.2                      | 134                         |
| S37                | 98              | Google Scholar    | Citation      | 4.4                      | 223                         |
| S38                | 444             | Google Scholar    | Citation      | 4.8                      | 32                          |
| S39                | 1729            | Google Scholar    | Citation      | 4.6                      | 731                         |
| S40                | 9               | IEEE Xplore       | Citation      | 4.6                      | 59                          |
| S41                | 1735            | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S42                | 1828            | Google Scholar    | Citation      | 4.5                      | 352                         |
| S43                | 69              | Google Scholar    | Citation      | 4.7                      | 105                         |
| S44                | 79              | Google Scholar    | Citation      | 4.6                      | 45                          |
| S45                | 216             | Google Scholar    | Citation      | 4.0                      | 45                          |
| S46                | 2724            | Google Scholar    | Citation      | 4.6                      | 743                         |
| S47                | 210             | Google Scholar    | Citation      | 4.8                      | 148                         |
| S48                | 130             | Google Scholar    | Citation      | 4.2                      | 302                         |
| S49                | 32              | Google Scholar    | Citation      | 4.9                      | 179                         |
| S50                | 1900            | GitHub            | Signatures    | N/A (non-book)           | N/A (non-book)              |
| S51                | 2               | Google Scholar    | Citation      | N/A (not sold on Amazon) | N/A (not sold on Amazon)    |
| S52                | 212             | Google Scholar    | Citation      | 4.5                      | 108                         |
| S53                | 77              | Google Scholar    | Citation      | 4.4                      | 53                          |
| S54                | 162             | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S55                | 61              | Google Scholar    | Citation      | N/A (not sold on Amazon) | N/A (not sold on Amazon)    |
| S56                | 304             | Google Scholar    | Citation      | 4.2                      | 425                         |
| S57                | 28              | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S58                | 516             | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S59                | 63189           | Google Scholar    | Citation      | N/A (non-book)           | N/A (non-book)              |
| S60                | 28              | Google Scholar    | Citation      | 4.4                      | 22                          |
