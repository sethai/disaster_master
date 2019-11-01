<template>
    <div class="container">
        <div class="row">
            <div class ="col-sm-10">
                <h1>Disaster Master</h1>
                <br><br>
                <button type="button" class="btn btn-outline-primary">Refresh</button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Date</th>
                            <th scope="col">Type</th>
                            <th scope="col">Location</th>
                            <th scope="col">Additional info</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(disaster, index) in disasters" :key="index">
                            <td>{{ disaster.date }}</td>
                            <td>{{ disaster.type }}</td>
                            <td>{{ disaster.location }}</td>
                            <td>{{ disaster.additional_info }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      disasters: [],
    };
  },
  methods: {
    getDisasters() {
      const path = 'http://localhost:5000/disasters';
      axios.get(path)
        .then((res) => {
          this.disasters = res.data.disasters;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getDisasters();
  },
};
</script>
