<template>
  <aside class="sidebar">
    <slot name="top"/>
    <NavLinks/>
    <SidebarLinks :depth="0" :items="items"/>
    <slot name="bottom"/>
  </aside>
</template>

<script>
import { defineComponent } from 'vue-demi'
import SidebarLinks from '@theme/components/SidebarLinks'
import NavLinks from '@theme/components/NavLinks'

export default defineComponent({
  name: 'Sidebar',
  components: { SidebarLinks, NavLinks },
  props: ['items']
})
</script>

<style lang="stylus">
.sidebar
  &&::-webkit-scrollbar
    width: 0
    height: 0
  .personal-info-wrapper
    display none
  ul
    padding 0
    //margin 0
    list-style-type none
    &.sidebar-links
      > li
        background $accentColor
  a
    display inline-block
  .nav-links
    display none
    border-bottom 1px solid var(--border-color)
    padding 0.5rem 0 0.75rem 0
    a
      font-weight 600
    .nav-item, .repo-link
      display block
      line-height 1.25rem
      font-size 1.1em
      padding 0.5rem 0 0.5rem 1.5rem
  & > .sidebar-links
    padding 0rem 0
    & > li > a.sidebar-link
      font-size 1em
      line-height 1.7
      font-weight 500
    & > li:not(:first-child)
      margin-top 2.5rem
	&.depth-0 > .sidebar-heading::before {
	    content: "";
        position: absolute;
        top: -0.92rem;
        left: 1.5rem;
        width: 13rem;
		height: 0.05rem;
        background: rgba(234,236,239,1);
    }	

@media (max-width: $MQMobile)
  .sidebar
    .personal-info-wrapper
      display block
    .nav-links
      display block
      .dropdown-wrapper .nav-dropdown .dropdown-item a.router-link-active::after
        top calc(1rem - 2px)
    & > .sidebar-links
      padding 0rem 0
</style>
