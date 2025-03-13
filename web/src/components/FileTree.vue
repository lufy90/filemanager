<template>
  <li>
    <div @click="toggle">
      {{ item.name }}<span v-if="item.is_dir">[{{ isOpen ? '-' : '+' }}]</span>
    </div>
    <ul v-if="isOpen">
      <div v-if="isGettingData">loading...</div>
      <div v-else>
        <file-tree
          v-for="(child, index) in item.children"
          :key="index"
          :root="child"
          @select="onSelected"
        ></file-tree>
      </div>
    </ul>
  </li>
</template>
<script setup lang="ts">
import { onBeforeUpdate, onMounted, ref } from 'vue'
import type { PropType } from 'vue'
import { ajax } from '../utils/request'
import type { FileTreeItem } from './models'

const props = defineProps({
  root: {
    type: Object as PropType<FileTreeItem>,
    required: true,
  },
})

const emit = defineEmits(['select'])

const isOpen = ref(false)
const getParams = ref({})
const isGettingData = ref(false)
const item = ref<FileTreeItem>({
  children: [],
  is_dir: false,
  path: '',
  name: '',
})
const toggle = async () => {
  if (item.value.is_dir) {
    isOpen.value = !isOpen.value
    if (isOpen.value) {
      getParams.value = { path: item.value.path }
      await getChildren()
      emit('select', item.value)
    }
  } else {
    emit('select', item.value)
  }
}

const onSelected = (data: FileTreeItem) => {
  emit('select', data)
}

const getChildren = async () => {
  isGettingData.value = true
  await ajax.get('/files', getParams.value).then((res) => {
    isGettingData.value = false
    item.value.children = res.data
  })
}

onMounted(() => {
  item.value = props.root
})

onBeforeUpdate(() => {
  item.value = props.root
})
</script>
