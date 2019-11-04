<template>
    <div class="container">
        <div class="row">
            <div class ="col-sm-10">
                <h1>Disaster Master</h1>
                <br>
                <div class="custom-control custom-checkbox">
                  <input type="checkbox" class="custom-control-input" v-model="sel_disaster"
                  value="earthquake" id="earthquake_id">
                  <label class="custom-control-label" for="earthquake_id">earthquakes</label>
                </div>
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
      const path = '/disasters';
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
