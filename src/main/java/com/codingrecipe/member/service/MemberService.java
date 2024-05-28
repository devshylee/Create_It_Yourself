package com.codingrecipe.member.service;

import com.codingrecipe.member.dto.MemberDTO;
import com.codingrecipe.member.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.ui.Model;

import java.util.List;

@Service
@RequiredArgsConstructor
public class MemberService {
    private final MemberRepository memberRepository;
    private final BCryptPasswordEncoder passwordEncoder;

    public int save(MemberDTO memberDTO) {
        // 회원가입 시 비밀번호 암호화
        String encodedPassword = passwordEncoder.encode(memberDTO.getMemberPassword());
        memberDTO.setMemberPassword(encodedPassword);
        return memberRepository.save(memberDTO);
    }

    public boolean login(MemberDTO memberDTO, Model model) {
        // 이메일로 회원 정보 조회
        MemberDTO loginMember = memberRepository.findByMemberEmail(memberDTO.getMemberEmail());
        // 조회된 회원 정보가 있고, 입력된 비밀번호가 암호화된 비밀번호와 일치하면 로그인 성공
        if (loginMember != null && passwordEncoder.matches(memberDTO.getMemberPassword(), loginMember.getMemberPassword())) {
            return true;
        } else {
            model.addAttribute("loginError", "이메일 또는 비밀번호가 틀렸습니다.");
            return false;
        }
    }

    public List<MemberDTO> findAll() {
        return memberRepository.findAll();
    }

    public MemberDTO findById(Long id) {
        return memberRepository.findById(id);
    }

    public void delete(Long id) {
        memberRepository.delete(id);
    }

    public MemberDTO findByMemberEmail(String loginEmail) {
        return memberRepository.findByMemberEmail(loginEmail);
    }

    public boolean update(MemberDTO memberDTO) {
        // 비밀번호가 입력되었을 때만 암호화하여 업데이트
        if (!memberDTO.getMemberPassword().isEmpty()) {
            String encodedPassword = passwordEncoder.encode(memberDTO.getMemberPassword());
            memberDTO.setMemberPassword(encodedPassword);
        } else {
            // 비밀번호가 입력되지 않은 경우에는 기존의 암호화된 비밀번호를 유지
            MemberDTO existingMember = memberRepository.findById(memberDTO.getId());
            memberDTO.setMemberPassword(existingMember.getMemberPassword());
        }
        int result = memberRepository.update(memberDTO);
        return result > 0;
    }



    public String emailCheck(String memberEmail) {
        MemberDTO memberDTO = memberRepository.findByMemberEmail(memberEmail);
        return (memberDTO == null) ? "ok" : "no";
    }
}
