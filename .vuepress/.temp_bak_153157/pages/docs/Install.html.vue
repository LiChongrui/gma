<template><div><h2 id="required" tabindex="-1"><a class="header-anchor" href="#required"><span>Required</span></a></h2>
<ul>
<li>System: <Badge text="Windows 10+" vertical='middle'/> 64-bit (amd64),<Badge text="8 GB+" vertical='middle'/> RAM.</li>
</ul>
<div class="custom-container warning"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v4"></path><path d="M12 16h.01"></path></g></svg><p class="custom-container-title">Note</p><p><strong>gma</strong> is currently <u><em>not supported MacOS, Linux or other platforms</em></u>.</p>
</div><ul>
<li>
<p>Python Version: <Badge text="3.12 ~ 3.14" vertical='middle'/></p>
</li>
<li>
<p>Third-party library: <a href="https://numpy.org/" target="_blank" rel="noopener noreferrer">NumPy<Badge text="2.4.0+"/><ExternalLinkIcon/></a>, <a href="https://pandas.pydata.org/" target="_blank" rel="noopener noreferrer">Pandas<Badge text="3.0.4+"/><ExternalLinkIcon/></a>, <a href="https://scipy.org/" target="_blank" rel="noopener noreferrer">SciPy<Badge text="1.18.0+ "/><ExternalLinkIcon/></a>, <a href="https://matplotlib.org/" target="_blank" rel="noopener noreferrer">Matplotlib<Badge text="3.10.0+"/><ExternalLinkIcon/></a>.</p>
</li>
</ul>
<div class="custom-container info"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M12 8h.01"></path><path d="M11 12h1v4h1"></path></g></svg><p class="custom-container-title">INFO</p><p><a href="https://gdal.org/en/stable/" target="_blank" rel="noopener noreferrer">GDAL<Badge text="3.12.4"/><ExternalLinkIcon/></a> is built into GMA by default, so no additional installation is required.</p>
</div><h2 id="installation" tabindex="-1"><a class="header-anchor" href="#installation"><span>Installation</span></a></h2>
<div class="language-bash line-numbers-mode" data-highlighter="prismjs" data-ext="sh" data-title="sh"><pre v-pre><code><span class="line">pip <span class="token function">install</span> gma</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="custom-container tip"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M12 8h.01"></path><path d="M11 12h1v4h1"></path></g></svg><p class="custom-container-title">TIP</p><p>PyPi Project: <a href="https://pypi.org/project/gma/" target="_blank" rel="noopener noreferrer">https://pypi.org/project/gma/<ExternalLinkIcon/></a></p>
</div><h2 id="verifying" tabindex="-1"><a class="header-anchor" href="#verifying"><span>Verifying</span></a></h2>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment">## Import version info</span></span>
<span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> __version__</span>
<span class="line"></span>
<span class="line"><span class="token comment">## Import selected modules</span></span>
<span class="line"><span class="token keyword">from</span> gma <span class="token keyword">import</span> climet<span class="token punctuation">,</span> crs<span class="token punctuation">,</span> driver<span class="token punctuation">,</span> gio<span class="token punctuation">,</span> math<span class="token punctuation">,</span> rsvi<span class="token punctuation">,</span> smc<span class="token punctuation">,</span> etools<span class="token punctuation">,</span> env<span class="token punctuation">,</span> const</span>
<span class="line"></span>
<span class="line"><span class="token comment">## Spatial plotting and built-in data</span></span>
<span class="line"><span class="token keyword">from</span> gma<span class="token punctuation">.</span>carto <span class="token keyword">import</span> plot<span class="token punctuation">,</span> inres</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


