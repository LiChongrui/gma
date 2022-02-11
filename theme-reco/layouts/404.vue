<template>
  <section class="theme-container">
    <article class="content">
      <h1>错误代码：404</h1>
      <blockquote>{{ getMsg() }}</blockquote>
      <router-link to="/">返回首页</router-link>
    </article>
  </section>
</template>

<script>

	const msgs = [
	'~页面飞了~',
	'~火星人把页面带走了~',
	'页面不爱了~',
	'啊！页面哪里去了~',
	'~页面有问题啊，给我反馈吧~'
	]

	export default {
	methods: {
	getMsg () {
	return msgs[Math.floor(Math.random() * msgs.length)]
	}
	}
	}
</script>

<style src="../styles/theme.styl" lang="stylus"></style>

<style lang="stylus">
.content
  margin 4rem auto 0
  max-width 800px
  padding 0 2rem
.mod_404
  .desc
    .desc_link
      display: inline-block
      // margin: 20px 0
      background: #424242!important
      color: #ffffff
      padding: 6px 20px!important
      text-decoration: none!important
      border-radius: 4px

@media screen and (max-width: 720px)
  .mod_404
    .desc
      margin: 50px 0
    .wrapper
      margin 0!important
      padding-top 20px
</style>

