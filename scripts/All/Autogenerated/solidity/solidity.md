

## <p>How do you declare an address variable with value 0, how about 1?</p>


<p>address zero_addy = address(0);<br>address one_addy = address(0x1);</p>


## <p>What are the three state variable visibility levels?</p>


<p>public<br>internal<br>private</p>


## <p>State Variable Visibility: Who can access <code>public</code> variables and how?</p>


<p>Can be accessed within the contract and from external contracts.</p>
<p>Different from internal in that compiler autogenerates a getter function.</p>
<pre><code class="language-js">contract <span class="token constant">C</span> <span class="token punctuation">{</span>
   uint <span class="token keyword">public</span> data <span class="token operator">=</span> <span class="token number">30</span><span class="token punctuation">;</span>
   <span class="token keyword">function</span> <span class="token function">x</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">public</span> <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
      data <span class="token operator">=</span> <span class="token number">3</span><span class="token punctuation">;</span> <span class="token comment">// internal access</span>
      <span class="token keyword">return</span> data<span class="token punctuation">;</span>
   <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
contract Caller <span class="token punctuation">{</span>
   <span class="token constant">C</span> c <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">C</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
   <span class="token keyword">function</span> <span class="token function">f</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">public</span> view <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
      <span class="token keyword">return</span> c<span class="token punctuation">.</span><span class="token function">data</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">//external access</span>
   <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>State Variable Visibility: Who can access <code>internal</code> state variables?</p>


<p>The current contract and derived contracts.</p><p><br>This is the default visibility level for state variables.</p>
<pre><code class="language-js">pragma solidity <span class="token operator">^</span><span class="token number">0.5</span><span class="token number">.0</span><span class="token punctuation">;</span>
contract <span class="token constant">C</span> <span class="token punctuation">{</span>
   uint internal iData<span class="token operator">=</span> <span class="token number">10</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

contract <span class="token constant">D</span> is <span class="token constant">C</span> <span class="token punctuation">{</span>
   <span class="token keyword">function</span> <span class="token function">y</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">public</span> <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
      iData <span class="token operator">=</span> <span class="token number">3</span><span class="token punctuation">;</span> <span class="token comment">// internal access</span>
      <span class="token keyword">return</span> iData<span class="token punctuation">;</span>
   <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>State Variable Visibility: Who can access <code>private</code> state variables?</p>


<p>Like internal variables but are not visibile from derived contracts.</p>
<p>AKA: Only accessible internally from the current contract NOT derived contractsc.</p>


## <p>What is the default visibility level for state variables?</p>


<p>Internal</p>
<p>Note: Internal state variables can only be accessed from within the contract they are defined in and in derived contracts.<br>They cannot be accessed externally.</p>


## <p>Does Private / Internal state variable visibility level prevent reading from outside of the contract?</p>


<p>The whole world carn still view this information from outside of the  blockchain.</p>
<p>It only prevents other contracts from reading / modifying the information.</p>


## <p>What are the four function visibility levels?</p>


<p>public: all can access<br>external: cannot be accessed internally, only externally</p>
<p>internal: only this contract and derived contracts can access<br>private: only this contract can access.</p>
<hr>
<p>private is a subset of internal<br>external is a subset of private</p>


## <p>What function visibility level should you use if you only want it to callable from outside of the contract, but not from inside? Should you do this and why?</p>


<p>external</p>
<p>Always use external if you don&#39;t need to call the function from within the same contract, saves gas!</p>


## <p>What function visibility level should you use if you only want it to be callable from within the contract?</p>


<p>private</p>


## <p>What function visibility level should you use if you want it to be callable from within the contract and all derived contracts?</p>


<p>internal</p>


## <p>What is the <code>this</code> keyword?</p>


<p>&quot;this&quot; refers to the current contract</p>
<p>address(this): contract&#39;s address<br>address(this).balance: amount of ether in the contract<br>this.function(): call function, even if marked external</p>


## <p>How do you call an external function from within the same contract? Is this a good idea?</p>


<p>this.function() lets you call a function, even if marked external</p>
<p>Bad Idea. Requires a real CALL to be executed which is gas intensive.</p>
<p><a href="https://ethereum.stackexchange.com/questions/19380/external-vs-public-best-practices">src</a></p>


## <p>To save gas, what is the rule of thumb for choosing between external or public funtions?</p>


<p>External functions cost less gas. Use instead of public if you expect it to only be called externally.</p>
<p>Use public if you need to call the function internally: (this.f() is costly)</p>
<p><a href="https://ethereum.stackexchange.com/questions/19380/external-vs-public-best-practices">src</a></p>


## <p>What are the two keywords that can be used on state variables to restrict state modifications? (And what are the benefits to using them?)</p>


<p>Constant<br>Immutable</p>
<p>Benefit: Saves gas compared to regular state variables.</p>


## <p>State Variable Modification Restrictions: Difference between constant and immutable?</p>


<p>Constant variables can never be changed after compilation.</p>
<p>Immutable variables can be set within the constructor.</p>


## <p>What are the two function state mutability levels?</p>


<p>view<br>pure</p>


## <p>What function state mutability level should you use if your function doesn&#39;t modify state?</p>


<p>view</p>
<pre><code class="language-js"><span class="token keyword">function</span> <span class="token function">f</span><span class="token punctuation">(</span><span class="token parameter">uint a<span class="token punctuation">,</span> uint b</span><span class="token punctuation">)</span> <span class="token keyword">public</span> view <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> a <span class="token operator">*</span> <span class="token punctuation">(</span>b <span class="token operator">+</span> <span class="token number">42</span><span class="token punctuation">)</span> <span class="token operator">+</span> block<span class="token punctuation">.</span>timestamp<span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>When do you mark your function as view?</p>


<p>When it doesnt modify state.</p>
<pre><code class="language-js"><span class="token keyword">function</span> <span class="token function">f</span><span class="token punctuation">(</span><span class="token parameter">uint a<span class="token punctuation">,</span> uint b</span><span class="token punctuation">)</span> <span class="token keyword">public</span> view <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    <span class="token keyword">return</span> a <span class="token operator">*</span> <span class="token punctuation">(</span>b <span class="token operator">+</span> <span class="token number">42</span><span class="token punctuation">)</span> <span class="token operator">+</span> block<span class="token punctuation">.</span>timestamp<span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>What function state mutability level should you use if your function doesn&#39;t read from or modify state?</p>


<p>pure</p>
<pre><code class="language-js"><span class="token keyword">function</span> <span class="token function">f</span><span class="token punctuation">(</span><span class="token parameter">uint a<span class="token punctuation">,</span> uint b</span><span class="token punctuation">)</span> <span class="token keyword">public</span> pure <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
   <span class="token keyword">return</span> a <span class="token operator">*</span> <span class="token punctuation">(</span>b <span class="token operator">+</span> <span class="token number">42</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>When do you mark your function as pure?</p>


<p>When is doesn&#39;t read from or modify state</p>
<pre><code class="language-js"><span class="token keyword">function</span> <span class="token function">f</span><span class="token punctuation">(</span><span class="token parameter">uint a<span class="token punctuation">,</span> uint b</span><span class="token punctuation">)</span> <span class="token keyword">public</span> pure <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
   <span class="token keyword">return</span> a <span class="token operator">*</span> <span class="token punctuation">(</span>b <span class="token operator">+</span> <span class="token number">42</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>What is the difference between a state and local variable (location in code)?</p>


<p>Global Variables aka state variables are declared outside of all functions.</p>
<p>Local Variables are declared inside a function.</p>


## <div><div>What is the difference between a state variable and a local variable (lifetime / data location)?</div></div>


<p>State variables are placed in Storage (written to the blockchain). This data is persistent. Every change is registered on the blockchain</p>
<p>Variables declared inside of a function are stored in memory. They are temporary, acessible only from within the function, and are discarded after function execution.</p>


## <p>What are the three data locations? Rank them in order of gas usage (high to low)</p>


<p>storage<br>memory<br>calldata</p>
<p>note: data locations are places where the EVM stores variables</p>


## <p>What are the two (high-level) variable types? (ex: array vs bool)</p>


<p>Reference Type (array)<br>Value Type (bool)</p>


## <p>What is the difference between value type and reference type?</p>


<p>Value types are always passed by value. They are always copied when used as function arguments or in assignments.</p>
<p>Reference type data (map, array, struct) can be modified through different names.(and you must specify a data location)</p>


## <p>What are the three reference types (dynamic data types)?</p>


<p>Array (including strings / bytes)<br>Mappings<br>Stucts</p>
<p><a href="https://blockheroes.dev/data-location-in-solidity/">src</a></p>


## <p>Function parameters (including return ones) must be in one of which two data locations?</p>


<p>Memory and Calldata. (Use calldata if it won&#39;t be modified to save gas)</p>


## <p>What do you need to specify when using reference type?</p>


<p>A data location (storage, memory, calldata)</p>


## <p>What is the difference between data locations: storage and memory?</p>


<p>Data in Storage is permanent and onchain. (Mad expensive)</p>
<p>Data in Memory is temporary, and discarded on function exit.</p>


## <p>What&#39;s the difference between data locations: memory and calldata?</p>


<p>Calldata is like memory but also specifies that the data cannot be modified.</p>
<p>(Memory variables are mutable and non-persistent)</p>


## <p>When should you set a function parameter as calldata? Is this a good idea?</p>


<p>When the parameter does not need to be modified.</p>
<p>Calldata is the cheapest and should be used whenever possible.</p>


## <p>For Value types: When assigning a storage variable the value of a memory/calldata variable (and vice versa), what happens?</p>


<p>A copy is created.</p>
<pre><code class="language-js">contract Contract <span class="token punctuation">{</span>
  uint <span class="token keyword">public</span> age<span class="token punctuation">;</span>

  <span class="token function">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">{</span>
     age <span class="token operator">=</span> <span class="token number">30</span><span class="token punctuation">;</span>
    <span class="token punctuation">}</span>

  <span class="token keyword">function</span> <span class="token function">changeAge</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">public</span> <span class="token function">returns</span><span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
     uint age2 <span class="token operator">=</span> age<span class="token punctuation">;</span> <span class="token comment">// assign storage -> memory creates copy</span>
     age <span class="token operator">=</span> <span class="token number">20</span><span class="token punctuation">;</span>
     <span class="token keyword">return</span> age2<span class="token punctuation">;</span> <span class="token comment">// returns 30</span>
  <span class="token punctuation">}</span>

<span class="token punctuation">}</span>
</code></pre>


## <p>When assigning data between value types from the same data location (ex: storage to storage), what happens?</p>


<p>A copy is created.</p>


## <p>For reference types, when assigning from one memory variable to another memory variable, what happens?</p>


<p>A reference is created. They will point to the same data location so if you modify one, it will reflect in both.</p>
<pre><code class="language-js">contract Contract <span class="token punctuation">{</span>
  <span class="token keyword">function</span> <span class="token function">vote</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">public</span> <span class="token function">returns</span><span class="token punctuation">(</span><span class="token parameter">uint<span class="token punctuation">[</span><span class="token punctuation">]</span> memory</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
    uint<span class="token punctuation">[</span><span class="token punctuation">]</span> memory ages <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">uint</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    ages<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token number">2</span><span class="token punctuation">;</span>
    ages<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token number">3</span><span class="token punctuation">;</span>

    uint<span class="token punctuation">[</span><span class="token punctuation">]</span> memory newages <span class="token operator">=</span> ages<span class="token punctuation">;</span> <span class="token comment">// assign reference memory variable to a reference memory variable</span>
    ages<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token number">7</span><span class="token punctuation">;</span>
    <span class="token keyword">return</span> newages<span class="token punctuation">;</span> <span class="token comment">// returns (7,3)</span>
  <span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>
<p>Note: Assigning from storage to local storage variables will also result in a reference.</p>


## <p>How do you convert a uint to string?</p>


<pre><code class="language-js"><span class="token keyword">import</span> <span class="token string">"@openzeppelin/contracts/utils/Strings.sol"</span><span class="token punctuation">;</span>
Strings<span class="token punctuation">.</span><span class="token function">toString</span><span class="token punctuation">(</span>myUINT<span class="token punctuation">)</span>
</code></pre>


## <p>How do you concatenate strings?</p>


<pre><code class="language-js">string<span class="token punctuation">.</span><span class="token function">concat</span><span class="token punctuation">(</span>s1<span class="token punctuation">,</span> s2<span class="token punctuation">)</span>
</code></pre>


## <p>What are the two function keyword types, and what order are they placed syntactically?</p>


<p>function f(uint a) 'VISIBILITY_LEVEL' 'STATE_MUTABILITY_LEVEL' returns (uint[] memory)</p>
<pre><code class="language-js"><span class="token keyword">function</span> <span class="token function">f</span><span class="token punctuation">(</span><span class="token parameter">uint a<span class="token punctuation">,</span> uint b</span><span class="token punctuation">)</span> <span class="token keyword">public</span> pure <span class="token function">returns</span> <span class="token punctuation">(</span><span class="token parameter">uint</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
   <span class="token keyword">return</span> a <span class="token operator">*</span> <span class="token punctuation">(</span>b <span class="token operator">+</span> <span class="token number">42</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>What Function Visibility Level should you use if you want everyone to be able to access it?</p>


<p>public</p>


## <p>How do you set a variable equal to a hexidecimal literal? (Include type for holding the variable)</p>


<pre><code class="language-js">bytes pubkey1 <span class="token operator">=</span> hex<span class="token string">"DEADBEEF"</span><span class="token punctuation">;</span>
</code></pre>
<p><a href="https://docs.soliditylang.org/en/develop/types.html#hexadecimal-literals">https://docs.soliditylang.org/en/develop/types.html#hexadecimal-literals</a></p>


## <p>What are the three ways to initialize a struct (Node, with id = 1, key = 2)?</p>


<pre><code class="language-js"><span class="token comment">// Method 1: Struct()</span>
Node n <span class="token operator">=</span> <span class="token function">Node</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">,</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token comment">// Method 2: Struct({})</span>
Node n <span class="token operator">=</span> <span class="token function">Node</span><span class="token punctuation">(</span><span class="token punctuation">{</span><span class="token literal-property property">id</span><span class="token operator">:</span><span class="token number">1</span><span class="token punctuation">,</span>key:<span class="token number">2</span><span class="token punctuation">}</span><span class="token punctuation">)</span>

<span class="token comment">// Method 3: n.key = value</span>
Node memory n<span class="token punctuation">;</span> <span class="token comment">// for temp data. use storage for  persistent data.</span>
n<span class="token punctuation">.</span>id <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">;</span>
n<span class="token punctuation">.</span>key <span class="token operator">=</span> <span class="token number">2</span><span class="token punctuation">;</span>
</code></pre>


## <p>How do you create a dynamic array &quot;recipients&quot; of addresses of size 2?</p>


<p>Use the &quot;new&quot; keyword.</p>
<pre><code class="language-js">address<span class="token punctuation">[</span><span class="token punctuation">]</span> memory recipients <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">address</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre>
