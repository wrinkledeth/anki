

## <p>How can you convert a to u32 and add it to b?</p>
<pre><code class="language-rust"><span class="token keyword">let</span> a <span class="token operator">=</span> <span class="token number">13u8</span><span class="token punctuation">;</span>
<span class="token keyword">let</span> b <span class="token operator">=</span> <span class="token number">7u32</span><span class="token punctuation">;</span>
<span class="token keyword">let</span> c <span class="token operator">=</span> <span class="token operator">?</span>
</code></pre>


<p>Use the &quot;as&quot; keyword</p>
<pre><code class="language-rust"><span class="token keyword">let</span> a <span class="token operator">=</span> <span class="token number">13u8</span><span class="token punctuation">;</span>
<span class="token keyword">let</span> b <span class="token operator">=</span> <span class="token number">7u32</span><span class="token punctuation">;</span>
<span class="token keyword">let</span> c <span class="token operator">=</span> a <span class="token keyword">as</span> <span class="token keyword">u32</span> <span class="token operator">+</span> b<span class="token punctuation">;</span>
</code></pre>


## <p>Style: how should you name variables and functions?</p>


<p>snake_case</p>


## <p>Style: how should you name constants?</p>


<p>SCREAMING_SNAKE_CASE</p>


## <p>create a constant called &quot;PI&quot; with the value 3.14</p>


<pre><code class="language-rust"><span class="token keyword">const</span> <span class="token constant">PI</span><span class="token punctuation">:</span> <span class="token keyword">f32</span> <span class="token operator">=</span> <span class="token number">3.14</span><span class="token punctuation">;</span>
</code></pre>
<h2 id=""></h2>
