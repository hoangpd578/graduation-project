@extends('dashboard.base')

@section('content')
        <div class="container-fluid">
          <div class="animated fadeIn">
            <div class="row">
              <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12">
                <div class="card">
                    <div class="card-header">
                      <i class="fa fa-align-justify"></i><strong>Công số</strong></div>
                    <div class="card-body">
                        <br>
                        <table class="table table-responsive-sm table-striped">
                        <thead>
                          <tr>
                            <th>#</th>
                            <th>Ngày</th>
                            <th>Thời gian bắt đầu</th>
                            <th>Thời gian kết thúc</th>
                            <th>Ảnh checkin</th>
                            <th>Ảnh checkout</th>
                            <th>Dự đoán checkin</th>
                            <th>Dự đoán checkout</th>
                          </tr>
                        </thead>
                        <tbody>
                          @foreach ($employees as $key => $employee)
                          <tr>
                            <td><strong>{{ ++$key }}</strong></td>
                            <td class='align-middle'>{{ $employee->work_date }}</td>
                            <td class='align-middle'>{{ $employee->check_in }}</td>
                            <td class='align-middle'>{{ $employee->check_out }}</td>
                            <td class='align-middle'><img src="{{ asset($employee->check_in_image) }}" alt="" style="width: 50px; height: 50px;"></td>
                            <td class='align-middle'><img src="{{ asset($employee->check_out_image) }}" alt="" style="width: 50px; height: 50px;"></td>
                            <td class='align-middle'>{{ $employee->prediction_checkin . '%' }}</td>
                            <td class='align-middle'>{{ $employee->prediction_checkout . '%'}}</td>
                          </tr>
                          @endforeach
                        </tbody>
                      </table>
                      <div class="paginate d-flex justify-content-center">
                        {{ $employees->links() }}
                      </div>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>

@endsection

@section('javascript')
    <script src="{{ asset('js/Chart.min.js') }}"></script>
    <script src="{{ asset('js/coreui-chartjs.bundle.js') }}"></script>
    <script src="{{ asset('js/main.js') }}" defer></script>
@endsection
