<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Employee;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\Controller;

class EmployeeController extends Controller
{
    public function index()
    {
        $userId = Auth::id();
        $employees = Employee::where('user_id', $userId)->paginate(10);
        

        return view('dashboard.timeSheet', ['employees' => $employees]);
    }

    public function show($id)
    {
        $employees = Employee::where('user_id', $id)->paginate(10);

        return view('dashboard.timeSheet', ['employees' => $employees]);
    }
}
