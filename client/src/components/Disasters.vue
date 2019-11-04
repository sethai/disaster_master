<template>
    <div class="container">
        <div class="row">
            <div class ="col-sm-10">
                <h1>Disaster Master</h1>
                <br>
                <input type="checkbox" checked v-model="sel_disaster" value="earthquake">earthquakes
                <br>
                <button type="submit" @click="reload()" class="btn btn-outline-primary">
                  Refresh
                </button>
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
      sel_disaster: [],
    };
  },
  methods: {
    getDisasters() {
      const path = 'http://localhost:5000/disasters';
      const params = {
        type: this.sel_disaster.toString(),
      };
      axios.get(path, { params })
        .then((res) => {
          this.disasters = res.data.disasters;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    reload() {
      this.getDisasters();
    },
  },
  created() {
    this.sel_disaster.push('earthquake');
    this.getDisasters();
  },
};
</script>
