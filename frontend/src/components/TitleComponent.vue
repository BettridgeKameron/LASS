<!-- MyComponent.vue -->
<template>
    <h1>{{ title }}</h1>
  </template>
  
  <script>
  export default {
    props: {
        title: String,
    },
    methods: {
        changeTitle(newTitle){
            this.$emit('updateTitle', newTitle);
        },
    },
  };
  </script>