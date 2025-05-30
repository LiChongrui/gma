<template>
  <section
    class="sidebar-group"
    :class="[
      {
        collapsable,
        'is-sub-group': depth !== 0
      },
      `depth-${depth}`
    ]"
  >
    <router-link
      v-if="item.path"
      class="sidebar-heading clickable"
      :class="{
        open,
        'active': isActive($route, item.path)
      }"
      :to="item.path"
      @click.native="$emit('toggle')"
    >
      <span>{{ item.title }}</span>
      <span
        class="arrow"
        v-if="collapsable"
        :class="open ? 'down' : 'right'">
      </span>
    </router-link>

    <p
      v-else
      class="sidebar-heading"
      :class="{ open }"
      @click="$emit('toggle')"
    >
      <span>{{ item.title }}</span>
      <span
        class="arrow"
        v-if="collapsable"
        :class="open ? 'down' : 'right'">
      </span>
    </p>

    <DropdownTransition>
      <SidebarLinks
        class="sidebar-group-items"
        :items="item.children"
        v-if="open || !collapsable"
        :sidebarDepth="item.sidebarDepth"
        :depth="depth + 1"
      />
    </DropdownTransition>
  </section>
</template>

<script>
import { defineComponent, getCurrentInstance } from 'vue-demi'
import { isActive } from '@theme/helpers/utils'
import DropdownTransition from '@theme/components/DropdownTransition'

export default defineComponent({
  name: 'SidebarGroup',
  props: ['item', 'open', 'collapsable', 'depth'],
  components: { DropdownTransition },

  setup (props, ctx) {
    const instance = getCurrentInstance().proxy

    instance.$options.components.SidebarLinks = require('./SidebarLinks.vue').default

    return { isActive }
  }
})
</script>

<style lang="stylus">
.sidebar-group
  background var(--background-color)
  .sidebar-group
    padding-left 0.5em
  &:not(.collapsable)
    .sidebar-heading:not(.clickable)
      cursor auto
      color var(--text-color)
  // refine styles of nested sidebar groups
  &.is-sub-group
    padding-left 0
    & > .sidebar-heading
      font-size 14px
      line-height 1.4
      font-weight bold
      padding-left 2.2rem
      &:not(.clickable)
        opacity 1
    & > .sidebar-group-items
      padding-left 1rem
      & > li > .sidebar-link
        font-size: 0.95em;
        border-left none
  &.depth-2
    & > .sidebar-heading
      border-left none

.sidebar-heading
  position relative
  color var(--text-color)
  transition color .15s ease
  cursor pointer
  font-size 16px
  font-weight bold
  padding 0.8rem 1.5rem 0.35rem 1.5rem
  width 100%
  box-sizing border-box
  margin 0
  &.open, &:hover
    color $accentColor
  .arrow
    position absolute
    top 0
    bottom 0
    right 1em
    margin auto
  &.clickable
    &.active
      font-weight 450
      color $accentColor
      border-left-color $accentColor
    &:hover
      color $accentColor

.sidebar-group-items
  transition height .1s ease-out
  font-size 0.95em
  overflow hidden
</style>
