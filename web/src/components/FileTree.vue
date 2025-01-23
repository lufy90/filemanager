<template>
    <li>
        <div :class="{bold: isFolder}" @click="toggle">{{ item.name }}<span v-if="isFolder">[{{ isOpen?"-":"+" }}]</span></div>
        <ul v-show="isOpen" v-if="isFolder">
            <file-tree v-for="(child,index) in item.children" :key="index" :root="child"></file-tree>
        </ul>
    </li>
</template>
<script setup lang="ts">

import {onMounted, ref} from 'vue'
import type { PropType } from 'vue';
import {ajax}  from "../utils/request" 

interface FileTreeItem {
    name: string;
    path: string;
    is_dir: boolean;
}
const props = defineProps({
    root: {
        type: Object as PropType<FileTreeItem>,
        required: true
    }
})

const isFolder = ref(false)
const isOpen = ref(false)
const getParams = ref({})
const isGettingData = ref(false);
const item = ref({
    children: [],
    is_dir: false,
    path:'',
    name:'',
})
const toggle = async () => {
    if (isFolder.value) {
        isOpen.value = !isOpen.value
        if (isOpen.value) {
            getParams.value = {path: item.value.path}
            await getChildren()
        }
    }
}

const getChildren = async () => {
    isGettingData.value = true
    await ajax.get('/files', getParams.value).then((res) => {
        isGettingData.value = false
        item.value.children = res.data
    })
}

onMounted(() => {
    item.value = {...props.root, children:[]}
    isFolder.value = item.value.is_dir
})
</script>