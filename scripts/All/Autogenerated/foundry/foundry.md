

## <p>How to initialize a new project?</p>


<pre><code class="language-bash">forge init  <span class="token comment"># Empty Folder</span>
forge init newApp <span class="token comment"># New folder</span>
</code></pre>


## <p>How to generate remappings?</p>


<p>forge remappings &gt; remappings.txt</p>


## <p>How to build / compile a project?</p>


<p>forge build</p>


## <p>How to execute tests?</p>


<p>forge test</p>


## <p>How do you increase verbosity on a test?</p>


<pre><code class="language-bash">forge <span class="token builtin class-name">test</span> -vvvv

Level <span class="token number">2</span> <span class="token punctuation">(</span>-vv<span class="token punctuation">)</span>: Logs emitted during tests are also displayed. That includes assertion errors from tests, showing information such as expected vs actual.
Level <span class="token number">3</span> <span class="token punctuation">(</span>-vvv<span class="token punctuation">)</span>: Stack traces <span class="token keyword">for</span> failing tests are also displayed.
Level <span class="token number">4</span> <span class="token punctuation">(</span>-vvvv<span class="token punctuation">)</span>: Stack traces <span class="token keyword">for</span> all tests are displayed, and setup traces <span class="token keyword">for</span> failing tests are displayed.
Level <span class="token number">5</span> <span class="token punctuation">(</span>-vvvvv<span class="token punctuation">)</span>: Stack traces and setup traces are always displayed.
</code></pre>


## <p>How do you access a contracts public variable using solidity?</p>


<pre><code class="language-js">string memory out <span class="token operator">=</span> contract<span class="token punctuation">.</span><span class="token function">variable</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>


## <p>How do you print data / variable contents to the console?</p>


<pre><code class="language-js"><span class="token comment">// Solidity Test</span>
emit <span class="token function">log</span><span class="token punctuation">(</span>data<span class="token punctuation">)</span>
<span class="token operator">--</span><span class="token operator">-</span>
<span class="token comment">// Forge Command</span>
forge test <span class="token operator">-</span>vv <span class="token comment">// prints emitted test logs</span>
</code></pre>


## <p>Cheatcode to set msg.sender to target address for the next call?</p>


<pre><code class="language-js"><span class="token comment">/// function withdraw() public {</span>
<span class="token comment">///     require(msg.sender == owner);</span>
vm<span class="token punctuation">.</span><span class="token function">prank</span><span class="token punctuation">(</span>owner<span class="token punctuation">)</span><span class="token punctuation">;</span>
myContract<span class="token punctuation">.</span><span class="token function">withdraw</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// [PASS]</span>
</code></pre>


## <p>Cheatcode to set msg.sender to target address for all subesquent calls? (+ how to end?)</p>


<pre><code class="language-js">address controller <span class="token operator">=</span> <span class="token function">address</span><span class="token punctuation">(</span><span class="token number">0x1</span><span class="token punctuation">)</span>
vm<span class="token punctuation">.</span><span class="token function">startPrank</span><span class="token punctuation">(</span>controller<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// START PRANK</span>
coordinator<span class="token punctuation">.</span><span class="token function">initialize</span><span class="token punctuation">(</span>nodes<span class="token punctuation">,</span> keys<span class="token punctuation">)</span><span class="token punctuation">;</span>
vm<span class="token punctuation">.</span><span class="token function">stopPrank</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// STOP PRANK</span>
</code></pre>


## <p>Cheatcode to set the block number?</p>


<pre><code class="language-js">vm<span class="token punctuation">.</span><span class="token function">roll</span><span class="token punctuation">(</span><span class="token number">100</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
emit <span class="token function">log_uint</span><span class="token punctuation">(</span>block<span class="token punctuation">.</span>number<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// 100</span>
</code></pre>


## <p>Cheatcode to set the block timestamp?</p>


<pre><code class="language-js">vm<span class="token punctuation">.</span><span class="token function">warp</span><span class="token punctuation">(</span><span class="token number">1641070800</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
emit <span class="token function">log_uint</span><span class="token punctuation">(</span>block<span class="token punctuation">.</span>timestamp<span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// 1641070800</span>
</code></pre>


## <p>Cheatcode to set an address&#39;s balance to 1 eth</p>


<pre><code class="language-js">vm<span class="token punctuation">.</span><span class="token function">deal</span><span class="token punctuation">(</span>addy<span class="token punctuation">,</span> <span class="token number">1</span> <span class="token operator">*</span> <span class="token number">10</span><span class="token operator">**</span><span class="token number">18</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre>


## <p>How to add a gas report to your test?</p>


<pre><code class="language-bash">forge <span class="token builtin class-name">test</span> --gas-report
</code></pre>


## <p>How to get a list of all test options?</p>


<pre><code class="language-bash">forge <span class="token builtin class-name">test</span> --help
</code></pre>


## <p>What do you name the corresponding test file for Contract.sol?</p>


<p>Contract.t.sol</p>


## <p>How to let forge know that a function is a test?</p>


<p>Any contract with a function that starts with &quot;test&quot; is considered to be a test.</p>


## <p>How to tell forge to re-run modified tests when files are changed?</p>


<pre><code class="language-bash">forge <span class="token builtin class-name">test</span> --watch
</code></pre>


## <p>How to re-run ALL tests when files are changed?</p>


<pre><code class="language-bash">forge <span class="token builtin class-name">test</span> --watch --run-all
</code></pre>


## <p>How do you generate ABI&#39;s and where are they located in the dir structure?</p>


<pre><code class="language-bash">forge build
</code></pre>
<p>They are located in thes &quot;out&quot; directory</p>


## <p>How do you tell forge to expect an error on the next call?</p>


<pre><code class="language-bash">vm.expectRevert<span class="token punctuation">(</span><span class="token string">"Expected Error Message"</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
</code></pre>


## <p>How do you tell forge to only test a specified contract?</p>


<p>forge test --match-contract <target contract></p>


## <p>How do you convert a uint256 to string?</p>


<pre><code class="language-js"><span class="token keyword">import</span> <span class="token string">"openzeppelin-contracts/contracts/utils/Strings.sol"</span><span class="token punctuation">;</span>
Strings<span class="token punctuation">.</span><span class="token function">toString</span><span class="token punctuation">(</span>myUINT<span class="token punctuation">)</span>
</code></pre>


## <p>How do you tell forge to only run a specific test?</p>


<p>forge test --match-test NodeRegister</p>
<pre><code class="language-js"><span class="token keyword">function</span> <span class="token function">testNodeRegister</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">public</span> <span class="token punctuation">{</span><span class="token punctuation">}</span>
</code></pre>


## <p>In your test file, where do you put code that you want to run before every test function?</p>


<pre><code class="language-js"><span class="token keyword">function</span> <span class="token function">setUp</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">public</span> <span class="token punctuation">{</span>
    vm<span class="token punctuation">.</span><span class="token function">deal</span><span class="token punctuation">(</span>controller<span class="token punctuation">,</span> <span class="token number">1</span> <span class="token operator">*</span> <span class="token number">10</span><span class="token operator">**</span><span class="token number">18</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
    vm<span class="token punctuation">.</span><span class="token function">prank</span><span class="token punctuation">(</span>controller<span class="token punctuation">)</span><span class="token punctuation">;</span>
    coordinator <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">Coordinator</span><span class="token punctuation">(</span><span class="token constant">THRESHOLD</span><span class="token punctuation">,</span> <span class="token constant">PHASE_DURATION</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>


## <p>What unit are forge gas estimates reported in? How do you convert to eth?</p>


<pre><code class="language-bash">Running <span class="token number">1</span> <span class="token builtin class-name">test</span> <span class="token keyword">for</span> test/RprAirdrop.t.sol:RPRTest
<span class="token punctuation">[</span>PASS<span class="token punctuation">]</span> testAirdropGas<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">(</span>gas: <span class="token number">4356679</span><span class="token punctuation">)</span>
</code></pre>
<p>Gas is reported in Gas Units (&quot;gallons of gas&quot;)</p>
<p>The price / gas unit can be found on <a href="https://etherscan.io/gastracker">Eth gas tracker</a> (around 10gwei / unit)</p>
<p>Total price in eth is determined during time of transaction.</p>
