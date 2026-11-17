<template lang="pug">
NLayoutFooter.global-footer(bordered)
  div(w-1200px, max-w='[calc(100vw-2rem)]', m-x-auto, p-t-6, p-b-10)
    NP Copyright © {{ date.getFullYear() }} {{ site.siteName || 'CloudVault' }}
    .flex.items-center.gap-2.flex-wrap
      NText
        | Powered by
        |
        NA(href='https://github.com/project-epb/cloudvault', target='_blank', rel='noopener noreferrer') CloudVault
      NText(depth='3') ·
      NText
        | Made with 🐟 by
        |
        NA(href='https://github.com/dragon-fish', target='_blank', rel='noopener noreferrer') Dragon Fish
</template>

<script setup lang="ts">
const date = useNow()
const site = useSiteStore()
</script>

<style scoped lang="sass"></style>
