<template>
  <q-page class="row items-center justify-evenly">
    <file-tree
      title="Example component"
      :root="item"
    ></file-tree>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import FileTree from '../components/FileTree.vue'
const item = ref({
  name: '/',
  path:'',
  is_dir:true,
})

</script>
