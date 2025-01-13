<script setup lang="ts">
import {ajax} from "@/utils/request";
import {onMounted, ref} from "vue";

const tableData = ref([]);
const isGettingData = ref(false);
const getParams = ref({});
const getData = () =>{
  isGettingData.value = true;
  ajax.get("/files",getParams.value).then((res) => {
    isGettingData.value = false;
    tableData.value = res.data;
  });
}

const columns = [
{ name: 'name', label: 'name', field: 'name' },
{name:'path',label:'path',field:'path'},
];

const onclick = (data) => {
  getParams.value = {
    path:data.path
  }
  getData();
}

onMounted(() => {
  getData();
});
</script>

<template>
  <main>
    <q-table
      title="files"
      :rows="tableData"
      :columns="columns"
      row-key="name"
    >
    <template v-slot:body-cell-name="scope">
      <q-btn flat :label="scope.row.name" color="primary" @click="onclick(scope.row)" />
    </template>
    </q-table>
  </main>
</template>
