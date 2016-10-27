### Team D

### Reference
Towards Discovering the Role of Emotions in Stack Overflow

### Keywords 

- **Code Example** - This specifies what kind of code is actually helpful to developers and maintainers to solve problems and which are not helpful to them.

- **Documentation** - This specifies that the documentation of the code in stack overflow answer is as important as the code itself.

- **API** -  Application program interface is a set of routines, protocols, and tools for building software applications. An API specifies how software components should interact and APIs are used when programming graphical user interface (GUI) components.

- **Social Learning** - It is a method of participating with others to make sense of new ideas. Sharing thoughts on stack overflow is a good example of social learning

### Notes

- **Study Instruments** - Data collected was from stack overflow. The code example selected was from the Q&A thread that <br>
  a. Contains an answer with relatively high score.<br>
  b. Answer should contain a code<br>
  Crawling done on 150000 pages and resulted in 497 pages with that attribute

- **Pattern** - These were the attributes of recognized answers
1. Consise code
2. Using question context
3. Highlighting important elements
4. Step-by-step solution
5. Providing links to extra resources

- **Informative visualizations**
<br/><br/>
<img src="screenshots/answerScores.png" alt="Drawing" width="50%" height="50%"/>
<img src="screenshots/questionTypes.png" alt="Drawing" width="50%" height="50%"/>
<img src="screenshots/codeContaining.png" alt="Drawing" width="50%" height="50%"/>

- **Future Work** - Findings were made that code examples and explanations are inseparable elements of recognized answers. Using these findings the author looks forward to combining the findings on automated tests and study their effects on developers learning experinece


### Needs Improvement

- Authors criteria for building our sample might be regarded as too restrictive (focusing on Java Q&A and using threads containing code examples with relatively high score). There might be a lot of recognized answers without code, but would barely provide much insight into reaching our goal.
- Another limiting assumption of their study was the score of answers. They assumed that answers with higher scores generally mean better solutions; however, other factors such as answer posting time, the question topic, and the responder identity might affect these numbers.
- The generalizability of our findings could be regarded as another limitation. 
