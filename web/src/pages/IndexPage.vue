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
        <file-tree :root="item"></file-tree>
      </ul>
    </q-drawer>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import FileTree from '../components/FileTree.vue'
const item = ref({
  name: '/',
  path: '',
  is_dir: true,
})

const openDrawer = ref(true)
</script>
