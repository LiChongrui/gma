<script>
import { defineComponent, computed, getCurrentInstance } from 'vue-demi'
import { isActive } from '@theme/helpers/utils'

export default defineComponent({
  setup (props, ctx) {
    const instance = getCurrentInstance().proxy

    const headers = computed(() => {
      return instance.$showSubSideBar ? instance.$page.headers : []
    })

    const isLinkActive = (header) => {
      const active = isActive(instance.$route, instance.$page.path + '#' + header.slug)
      if (active) {
        setTimeout(() => {
          document.querySelector(`.reco-side-${header.slug}`).scrollIntoView()
        }, 300)
      }
      return active
    }

    return { headers, isLinkActive }
  },
  render (h) {
    return h('ul', {
      class: { 'sub-sidebar-wrapper': true },
      style: { width: this.headers.length > 0 ? '12rem' : '0' }
    }, [
      ...this.headers.map(header => {
        return h('li', {
          class: {
            active: this.isLinkActive(header),
            [`level-${header.level}`]: true
          },
          attr: { key: header.title }
        }, [
          h('router-link', {
            class: { 'sidebar-link': true, [`reco-side-${header.slug}`]: true },
            props: { to: `${this.$page.path}#${header.slug}` }
          }, header.title)
        ])
      })
    ])
  }
})
</script>

<style lang="stylus" scoped>
.sub-sidebar-wrapper
  width 16rem !important
  padding-left 0
  list-style none
  font-size 12px
  right 0rem
  li
    padding 0.12rem 0
    cursor pointer
    border-left 1px solid var(--border-color)
    a
      padding 0.35rem 1rem 0.35rem 0rem
      color var(--text-color)
    &:hover
      a
       color $accentColor
    &.active
      border-left 1px solid $accentColor 
      a
       color $accentColor
       font-weight 550
    &.level-1
      padding-left .4rem
    &.level-2
      padding-left .8rem
    &.level-3
      padding-left 1.6rem
</style>

