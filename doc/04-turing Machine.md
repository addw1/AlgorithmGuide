# Truing Machine

### **Intro**

![image-20241215001822977](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215001822977.png)

​														**Figure1: Turing machine**

:one: **Read and write on tape**
:two:**​ Move both way on tape**
:three: **Access to infinite tape**
:four:**​ Accept or reject any time**(not only at the end of the input)

>**In one step the TM can:**
>	Change the state
>	R/W on tape under the head
>	Move one cell to the left or right

![image-20241215002738116](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215002738116.png)

​													**Figure2: One step Opeartion**



**TM example**

TM recognizing $L = {(a^nb^nc^n | n: n ≥ 0)}$

1. Scan right until `_` while checking if input is in $a^*b^*c^*$ , Reject if not 
2. Scan right, crossing off ==single== a, b, and c. 
3. If the last one of each symbol -> Accept
4. If the last one of some symbol but not others -> Reject 
5. If all symbols remain, return to left end and repeat from (3)

![image-20241215004252110](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215004252110.png)

​												          **Figure3: Answer for question 1**

​			

### **TM Formal Definition**

<font>Definition</font>
A TM is a 7-tuples $(Q, Σ, Γ, δ, q_0, q_{accept}, q_{reject})$ 

1. Q is a finite, non-empty set of states 
2. Σ is the input alphabet. Blank symbol _ ∉ Σ 
3. Γis the tape alphabet  (Σ⊆Γ and _∈ Γ)  
4.  δ:  Q×Γ→Q×Γ× {L, R}  is the transition function 
5.  q0∊Q is the start state 
6.  $q_{accept}$∊Q is the accept state 
7.  $q_{reject}$∊Q is the reject state

<blockquote alt="danger"><p>Unlike Finite Automata and Pushdown Automata, TM  may never halt!
    It may continues to run forever without  entering accept or reject states.</p></blockquote>

![image-20241215005703757](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215005703757.png)

​													**Figure4: TM running forever**



**TM Configuration**

<font title="red">Configuration </font>
A configuration of a TM specifies current contents  of tape, state, and head position.

Configurations are represented as u q v where q ∊Q and u, v  ∊ Γ* (u and v are strings over the tape alphabet)

<img src="C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215010030289.png" alt="image-20241215010030289" style="zoom:67%;" />

​												            **Figure5: TM Configuration**

A configuration <span alt="wavy">C</span> yields a configuration <span alt="wavy">C’</span> if a TM goes from C to C’ in one step.

<img src="C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215010429612.png" alt="image-20241215010429612" style="zoom: 67%;" />

<span alt="solid">Start configuration</span> of M on input w Accept configuration is $q_0w$ 

<span alt="solid">Accept configuration</span> of M on input w is  $q_{accpet}$

<span alt="solid">Reject configuration</span> of M on input w is  $q_{recject}$

<span alt="solid">Halt configuration</span> of M on input w is $q_{recject}$ or $q_{accept}$

<kbd>More</kbd>

A Turing Machine M accepts (rejects, halts  on) input w if a sequence of configurations C1,C2, …, Ck exists where:

1. $C_1$ is the start configuration 
2.  $C_i$ yields $C_{i+1} ∀ i < k$  
3. $C_k$ is an accept (rejects, halt) configuration



### Turing Decidable

<font>Definition</font> 
L is Turing-decidable if L= L(M) for some TM  decider M (if there exists a Turing machine M that decides it)
If ∃ a TM M such that for every input w: 
:car: w ∈L ⇒M accepts w 
:bread: w ∉L ⇒M rejects w



### Question

1. <span alt="solid">Give the sequence of configurations</span> that Turing machine M1 enters when started on input string 110#11.
   M1 = (Q, Σ, Γ, δ, q1, qaccept, qreject)

   >• Q = {q1, q2, ..., q8, qaccept, qreject}
   >• Σ = {0, 1, #}
   >• Γ = {0, 1, #, x, }
   >
   >• We describe δ with a table and a state diagram (see the following table and figure)
   >• The start, accept, and reject states are q1, qaccept, and qreject respectively.

![image-20241215011749825](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215011749825.png)

To simplify the figure, we don’t show the reject state or the transitions going to the reject state. Those transitions occur
implicitly whenever a state lacks an outgoing transition for a particular symbol. Thus because in state q5 no outgoing arrow
with a # is present, if a # occurs under the head when the machine is in state q5, it goes to qreject.

![image-20241215013506612](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241215013506612.png)



2. For the language A = {$w$#$w^R$ : w ∈ {0, 1}∗}:
   (a) Describe an algorithm (implementation-level description) for a Turing Machine that decides A.
   (b) Formally define your Turing machine. Describe the transition function with a table or a state diagram.









