<template>
  <q-page class="row items-center justify-evenly">
    <div class="absolute" style="top: 50px; left: -17px">
      <q-btn
        icon="chevron_right"
        round
        dense
        unelevated
        color="blue-13"
        @click="openDrawer = true"
      />
    </div>
    <q-drawer v-model="openDrawer" side="left" overlay behavior="desktop" elevated>
      <div class="absolute" style="top: 50px; right: -17px">
        <q-btn
          icon="chevron_left"
          round
          dense
          unelevated
          color="blue-13"
          @click="openDrawer = false"
        />
      </div>
      <ul>
        <file-tree :root="item" @select="handleChange"></file-tree>
      </ul>
    </q-drawer>
    <div class="main">
      <ContentView :data="currentItem" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import FileTree from '../components/FileTree.vue'
import type { FileTreeItem } from '../components/models'
import ContentView from '../components/ContentView.vue'

const item = ref<FileTreeItem>({
  name: '/',
  path: '',
  is_dir: true,
  children: [],
})

const currentItem = ref<FileTreeItem>({
  name: '/',
  path: '',
  is_dir: true,
  children: [],
})

const handleChange = (selected: FileTreeItem) => {
  console.log('selected:', selected)
  currentItem.value = selected
}

const openDrawer = ref(true)
</script>
<style lang="css">
.main {
  width: calc(100% - 200px);
  height: 100%;
  overflow: auto;
}
</style>
