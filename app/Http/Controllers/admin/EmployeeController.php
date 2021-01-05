<?php

namespace App\Http\Controllers\admin;

use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\Controller as BaseController;

class EmployeeController extends BaseController
{
    public function index()
    {
        $users = User::paginate(10);

        return view('dashboard.homepage', ['users' => $users]);
    }
}
